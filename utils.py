import urllib.request
from typing import Dict, Any


def build_url(base_url: str, params: Dict[str, Any]) -> str:
    return base_url + "?" + urllib.parse.urlencode(params)
