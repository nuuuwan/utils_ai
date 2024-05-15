import tempfile

from utils_base import Log
from utils_www import WWW

log = Log('GenericAIImage')


class GenericAIImage:
    def get_image_url(self, prompt: str) -> str:
        raise NotImplementedError

    def draw(self, prompt: str):
        try:
            image_url = self.get_image_url(prompt)
            image_path = tempfile.mktemp('.png')
            WWW.download_binary(image_url, image_path)
            return image_path
        except Exception as e:
            log.error(str(e))
            return None
