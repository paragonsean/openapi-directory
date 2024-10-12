from typing import List, Dict
from aiohttp import web

from openapi_server.models.similar_get200_response import SimilarGet200Response
from openapi_server import util


async def similar_get(request: web.Request, link, page=None) -> web.Response:
    """Send a company website to receive a list of companies related to them.

    

    :param link: We&#39;ll provide information about related companies based on the site you provide. If a LinkedIn page is sent, we will try to identify the company related to the page. Ex. https://api.byautomata.io/similar?link&#x3D;ibm.com
    :type link: dict | bytes
    :param page: Page number of search results. Ex. https://api.byautomata.io/similar?link&#x3D;ibm.com&amp;page&#x3D;1
    :type page: dict | bytes

    """
    link = .from_dict(link)
    page = .from_dict(page)
    return web.Response(status=200)
