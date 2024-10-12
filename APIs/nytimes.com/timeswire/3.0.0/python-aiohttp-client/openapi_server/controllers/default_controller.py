from typing import List, Dict
from aiohttp import web

from openapi_server.models.content_json_get200_response import ContentJsonGet200Response
from openapi_server import util


async def content_json_get(request: web.Request, url) -> web.Response:
    """content_json_get

    

    :param url: The complete URL of a specific news item, URL-encoded or backslash-escaped
    :type url: str

    """
    return web.Response(status=200)


async def content_source_section_json_get(request: web.Request, source, section, limit=None, offset=None) -> web.Response:
    """content_source_section_json_get

    

    :param source: Limits the set of items by originating source  all &#x3D; items from both The New York Times and The International New York Times nyt &#x3D; New York Times items only iht &#x3D; International New York Times items only 
    :type source: str
    :param section: Limits the set of items by one or more sections all | One or more section names, separated by semicolons   To get all sections, specify all. To get a particular section or sections, use the section names returned by this request:  http://api.nytimes.com/svc/news/v3/content/section-list.json 
    :type section: str
    :param limit: Limits the number of results, between 1 and 20
    :type limit: int
    :param offset: Sets the starting point of the result set
    :type offset: int

    """
    return web.Response(status=200)


async def content_source_section_time_period_json_get(request: web.Request, source, section, time_period, limit=None, offset=None) -> web.Response:
    """content_source_section_time_period_json_get

    

    :param source: Limits the set of items by originating source  all &#x3D; items from both The New York Times and The International New York Times nyt &#x3D; New York Times items only iht &#x3D; International New York Times items only 
    :type source: str
    :param section: Limits the set of items by one or more sections all | One or more section names, separated by semicolons   To get all sections, specify all. To get a particular section or sections, use the section names returned by this request:  http://api.nytimes.com/svc/news/v3/content/section-list.json 
    :type section: str
    :param time_period: Limits the set of items by time published, integer in number of hours
    :type time_period: int
    :param limit: Limits the number of results, between 1 and 20
    :type limit: int
    :param offset: Sets the starting point of the result set
    :type offset: int

    """
    return web.Response(status=200)
