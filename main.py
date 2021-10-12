from fastapi import Depends, FastAPI
from functools import lru_cache
import config
from pydantic import IPvAnyAddress
from helper import get_ip_information

app = FastAPI()

@lru_cache()
def get_settings():
    return config.Settings()

@app.get('/ip/{ip}')
def get_ip_info(ip: IPvAnyAddress, settings: config.Settings = Depends(get_settings)):
    '''
    Description: This endpoint allows you to fetch information about any IPv4 or IPv6
    '''
    response = {}
    ip_details, status_code = get_ip_information(settings.request_url.format(ip))
    if ip_details.get('bogon'):
        response['message'] = "This is a bogon IP. Find more info about bogon IPs on https://ipinfo.io/bogon"
    response['ip'] = ip_details.get('ip')
    response['city'] = ip_details.get('city')
    return response