# api_client.py

import os
import base64
import time
from openai import OpenAI
from typing import Union, List
import itertools


class OpenAIImageQAClient:
    def __init__(
        self,
        api_key="EMPTY",
        base_url=None,
        model_name="/data1/zhangxinyu/Final-Project/models/Idefics2-8b",
        system_prompt="",
        temperature=0,
        max_tokens=64,
        timeout=120
    ):
        self.api_key = api_key
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        
        # 处理 base_url 列表
        if isinstance(base_url, str):
            self.base_urls = [base_url]
        elif isinstance(base_url, list):
            if not base_url:
                raise ValueError("base_url list cannot be empty")
            self.base_urls = base_url
        else:
            raise ValueError("base_url must be a string or a list of strings")
        
        # === 新增：判断是否为本地 vLLM 服务 ===
        # 规则：只要任一 base_url 包含 localhost / 127.0.0.1 / 0.0.0.0，就认为是本地
        self.is_local_vllm = any(
            "localhost" in url or 
            "127.0.0.1" in url or
            "0.0.0.0" in url
            for url in self.base_urls
        )

        self.url_iterator = itertools.cycle(self.base_urls)
        self.clients = {
            url: OpenAI(api_key=self.api_key, base_url=url, timeout=self.timeout)
            for url in self.base_urls
        }

    @staticmethod
    def _encode_image_base64(image_path):
        suffix = image_path.split('.')[-1].lower()
        if suffix not in ['jpg', 'jpeg', 'png', 'webp']:
            suffix = 'png'
        mime_type = "image/jpeg" if suffix in ('jpg', 'jpeg') else f"image/{suffix}"
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8"), mime_type
        
    def infer(self, image_paths: Union[str, List[str]], user_prompt):
        if isinstance(image_paths, str):
            image_paths = [image_paths]
        
        current_url = next(self.url_iterator)
        client = self.clients[current_url]
        start_time = time.time()

        content_list = []
        
        if image_paths:
            for img_path in image_paths:
                if not os.path.exists(img_path):
                    raise FileNotFoundError(f"Image not found: {img_path}")
                
                if self.is_local_vllm:
                    # ✅ 本地 vLLM：直接传 file:// 路径
                    abs_path = os.path.abspath(img_path)
                    url = f"file://{abs_path}"
                    content_list.append({
                        "type": "image_url",
                        "image_url": {"url": url}
                    })
                else:
                    # ✅ 远程 API（OpenAI等）：必须 base64
                    image_b64, mime_type = self._encode_image_base64(img_path)
                    url = f"data:{mime_type};base64,{image_b64}"
                    content_list.append({
                        "type": "image_url",
                        "image_url": {"url": url}
                    })
        
        content_list.append({"type": "text", "text": user_prompt})

        try:
            response = client.chat.completions.create(
                model=self.model_name,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": content_list}
                ]
            )
        except Exception as e:
            raise RuntimeError(f"Request failed on {current_url}: {str(e)}")

        latency = time.time() - start_time
        raw_text = (response.choices[0].message.content or "").strip()

        usage = None
        if hasattr(response, "usage") and response.usage:
            usage = response.usage.model_dump()

        return {
            "raw_text": raw_text,
            "latency": latency,
            "usage": usage,
            "used_url": current_url
        }