

from artemis.backend.core.simplerest import SimpleRestClient


class SimpleRestTest():
    def __init__(self, content: str):
        self.client = SimpleRestClient()