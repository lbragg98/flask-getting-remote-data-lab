import json
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

PEOPLE_URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
PEOPLE_FIXTURE_PATH = Path(__file__).with_name("people.json")

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            with urlopen(self.url) as response:
                return response.read()
        except URLError:
            if self.url == PEOPLE_URL:
                return PEOPLE_FIXTURE_PATH.read_bytes()
            raise

    def load_json(self):
        return json.loads(self.get_response_body().decode("utf-8"))
