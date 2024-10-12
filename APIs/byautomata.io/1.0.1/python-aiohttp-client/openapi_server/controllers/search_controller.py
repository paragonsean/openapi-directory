from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_get200_response import SearchGet200Response
from openapi_server import util


async def search_get(request: web.Request, terms, page=None) -> web.Response:
    """Send search terms to receive the most relevant companies along with text snippets.

    

    :param terms: We provide information about related companies based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/search?link&#x3D;cloud+computing,enterprise,security
    :type terms: dict | bytes
    :param page: Page number of search results. Ex. https://api.byautomata.io/search?page&#x3D;0&amp;link&#x3D;cloud+computing,enterprise,security
    :type page: dict | bytes

    """
    terms = .from_dict(terms)
    page = .from_dict(page)
    return web.Response(status=200)
