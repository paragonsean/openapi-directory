from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_search_0(request: web.Request, q, size=None, _from=None, filter=None) -> web.Response:
    """Search for a disease or a target

    This method allows you to look for gene or diseases of interest using a free text search, replicating the functionality of the search box on our homepage. It should be used to identify the best match for a disease or target of interest, rather than gathering a specific set of evidence. 

    :param q: A full text query.
    :type q: str
    :param size: Maximum amount of results to return. Defaults to 10, max is 10000.
    :type size: str
    :param _from: How many initial results should be skipped. Defaults to 0.
    :type _from: str
    :param filter: Restrict the search to the type requested. Eg. &#x60;target&#x60; or &#x60;disease&#x60;.
    :type filter: str

    """
    return web.Response(status=200)
