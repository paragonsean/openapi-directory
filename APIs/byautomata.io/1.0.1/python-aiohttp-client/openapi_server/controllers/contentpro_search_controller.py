from typing import List, Dict
from aiohttp import web

from openapi_server.models.contentpro_search_get200_response import ContentproSearchGet200Response
from openapi_server import util


async def contentpro_search_get(request: web.Request, terms) -> web.Response:
    """Send search terms to receive the most relevant articles and companies.

    

    :param terms: We provide information about related companies and articles based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/contentpro-search?terms&#x3D;cloud+computing,enterprise,security
    :type terms: dict | bytes

    """
    terms = .from_dict(terms)
    return web.Response(status=200)
