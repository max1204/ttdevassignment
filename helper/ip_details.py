import httpx
import json

def get_ip_information(url):
    r = httpx.get(url)
    return json.loads(r.content), r.status_code