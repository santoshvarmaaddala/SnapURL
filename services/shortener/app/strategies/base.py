from abc import ABC, abstractmethod

class SlugGenerator(ABC):     # interface or abstract class for Url Generator algo
    @abstractmethod
    def generate(self, url: str) -> str:
        pass