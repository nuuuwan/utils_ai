import random

from utils_ai.providers.OpenAIProvider import OpenAIProvider


class ProviderFactory:
    PROVIDER_LIST = [
        OpenAIProvider,
    ]

    @staticmethod
    def random():
        provider = random.choice(ProviderFactory.PROVIDER_LIST)
        return provider()

    @staticmethod
    def from_name(name: str):
        if name == OpenAIProvider.NAME:
            return OpenAIProvider()
        raise ValueError(f"Unknown provider name: {name}")
