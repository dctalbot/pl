import urllib.request
import json


def get_html(url: str) -> str:
    resp = urllib.request.urlopen(url)
    result = json.loads(resp.read().decode("utf-8"))
    return result["parse"]["text"]
