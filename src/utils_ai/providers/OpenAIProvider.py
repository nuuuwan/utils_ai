import os
from openai import OpenAI

from utils_ai.generic_ai import GenericAI


class OpenAIProvider(GenericAI):
    NAME = "OpenAI"
    MODEL = "gpt-4o"
    IMAGE_MODEL = "dall-e-3"

    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_chat_reply(self, messages: list) -> str:
        response = self.client.chat.completions.create(
            model=self.MODEL,
            messages=messages,
        )
        return response.choices[0].message.content

    def get_image_url(self, prompt: str) -> str:
        response = self.client.images.generate(
            model=self.IMAGE_MODEL,
            prompt=prompt,
            size="1024x1024",
            n=1,
        )
        return response.data[0].url
