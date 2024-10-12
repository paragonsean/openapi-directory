from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def ip_geolocation_with_confidence_area_and_hazard_report_api(request: web.Request, ip=None, locality_language=None, key=None) -> web.Response:
    """IP Geolocation with Confidence Area and Hazard Report API

    This API returns additional security hazard report in addition to confidence area and locality information.

    :param ip: IPv4 IP address in a string or numeric format. If omitted, the caller’s IP address is assumed 
    :type ip: str
    :param locality_language: Preferred language for locality names in ISO 639-1 format, such as &#39;en&#39; for English, &#39;es&#39; for Spanish etc. Please note: 147 common world languages are supported, full list here, but not all languages are available for every location. If requested language is not available for a requested location it will default to English, if no English is available, the native, local names will be provided 
    :type locality_language: str
    :param key: Your API key 
    :type key: str

    """
    return web.Response(status=200)


async def ip_geolocation_with_confidence_area_api(request: web.Request, ip=None, locality_language=None, key=None) -> web.Response:
    """IP Geolocation with Confidence Area API

    Returns list of geocoordinates which represents estimated geolocation confidence area.

    :param ip: IPv4 IP address in a string or numeric format. If omitted, the caller’s IP address is assumed 
    :type ip: str
    :param locality_language: Preferred language for locality names in ISO 639-1 format, such as &#39;en&#39; for English, &#39;es&#39; for Spanish etc. Please note: 147 common world languages are supported, full list here, but not all languages are available for every location. If requested language is not available for a requested location it will default to English, if no English is available, the native, local names will be provided 
    :type locality_language: str
    :param key: Your API key 
    :type key: str

    """
    return web.Response(status=200)
