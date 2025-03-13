import httpx
from artemis.backend.constant.rest import HttpMethod


class SimpleRestClient:
    def __init__(self, method: HttpMethod, url: str, header: str, content=None):
        self.method = method.value
        self.url = url
        self.header = header

    def execute(self) -> httpx.Response:
        with httpx.Client() as client:
            match self.method:
                case "POST":
                    response = client.post(
                        url=self.url, headers=self.header, content=self.content
                    )
                case "GET":
                    response = client.get(url=self.url, headers=self.header)
                case _:
                    response = None

        return response
