from strategies.base import SlugGenerator
import requests

class ShortnerService:

    def __init__(self, strategy: SlugGenerator, storage_url: str) -> None:
        self.strategy = strategy
        self.stroage_url = storage_url


    def shorten_url(self, original_url: str):
        slug = self.strategy.generate(original_url)

        # Send to url-storage microservice
        response = requests.post(
            f"{self.stroage_url}/store",
            params = {"code": slug, "original_url": original_url}
        )

        if response.status_code == 200:
            return {"shortcode": slug}
        else: 
            raise Exception("Failed to Store Url")