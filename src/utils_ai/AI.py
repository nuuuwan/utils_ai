import os

import openai

from utils_ai.AIExecute import AIExecute
from utils_ai.AIImage import AIImage
from utils_ai.AIText import AIText


class AI(AIText, AIImage, AIExecute):
    def __init__(self):
        AIText.__init__(self)
        AIImage.__init__(self)
        AIExecute.__init__(self)

        openai.api_key = os.getenv("OPENAI_API_KEY")  # noqa
