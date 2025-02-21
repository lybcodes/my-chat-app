import os
from openai import OpenAI

class ChatModel:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

    def generate_response(self, message: str) -> str:
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]

        completion = self.client.chat.completions.create(
            model="qwen-max-2025-01-25",  # 使用通义千问模型
            messages=messages,
        )

        response = completion.choices[0].message.content
        return response

