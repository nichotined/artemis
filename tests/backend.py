from artemis.backend.constant.rest import HttpMethod
from artemis.backend.core.simplerest import SimpleRestClient


if __name__ == "__main__":
    response = SimpleRestClient(
        HttpMethod.GET,
        "https://api.restful-api.dev/objects",
        {"content": "application/json"},
    ).execute()
    print(response.content)
