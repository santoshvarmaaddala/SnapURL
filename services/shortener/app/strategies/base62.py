from .base import SlugGenerator
import string
import random

class Base62Generator(SlugGenerator):

    def __init__(self, length: int = 6) -> None:
        self.length = length
        self.alphabet = string.ascii_letters + string.digits

    def generate(self, url: str) -> str:
        return ''.join(random.choices(self.alphabet, k=self.length))