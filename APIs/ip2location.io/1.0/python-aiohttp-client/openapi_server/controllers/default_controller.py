from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def root_get(request: web.Request, key, ip, format=None, lang=None) -> web.Response:
    """root_get

    Geolocate user&#39;s location information via IP address

    :param key: API key.
    :type key: str
    :param ip: IP address (IPv4 or IPv6) for reverse IP location lookup purposes. If not present, the server IP address will be used for the location lookup.
    :type ip: str
    :param format: Format of the response message.
    :type format: str
    :param lang: Translation information. The translation only applicable for continent, country, region and city name. This parameter is only available for Plus and Security plan only.
    :type lang: str

    """
    return web.Response(status=200)
