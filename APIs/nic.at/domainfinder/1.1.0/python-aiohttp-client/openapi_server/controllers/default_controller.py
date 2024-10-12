from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v1_suggest_get200_response import ApiV1SuggestGet200Response
from openapi_server import util


async def api_v1_suggest_get(request: web.Request, term) -> web.Response:
    """Get .at domain name suggestions

    Provides a list of available .at domain names related to the given input term or domain

    :param term: Domainname/term to obtain suggestions for
    :type term: str

    """
    return web.Response(status=200)
