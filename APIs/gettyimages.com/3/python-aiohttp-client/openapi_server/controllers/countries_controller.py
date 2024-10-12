from typing import List, Dict
from aiohttp import web

from openapi_server.models.countries_list import CountriesList
from openapi_server import util


async def v3_countries_get(request: web.Request, accept_language=None) -> web.Response:
    """Gets countries codes and names.

    Returns a list of country objects that contains country name, two letter ISO abbreviation and three letter ISO abbreviation.  You&#39;ll need an API key and access token to use this resource. 

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str

    """
    return web.Response(status=200)
