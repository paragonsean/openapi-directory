from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def root_get(request: web.Request, ip, key, package=None, addon=None, format=None, lang=None) -> web.Response:
    """root_get

    Get geolocation information via IP address

    :param ip: IP address (IPv4 or IPv6) for reverse IP location lookup purpose. If not present, the server IP address will be used for the location lookup.
    :type ip: str
    :param key: API Key. Please sign up free trial license key at ip2location.com
    :type key: str
    :param package: Web service package of different granularity of return information.
    :type package: str
    :param addon: Extra information in addition to the above selected package.
    :type addon: List[str]
    :param format: Format of the response message.
    :type format: str
    :param lang: Translation information. The translation only applicable for continent, country, region and city name for the addon package.
    :type lang: str

    """
    return web.Response(status=200)
