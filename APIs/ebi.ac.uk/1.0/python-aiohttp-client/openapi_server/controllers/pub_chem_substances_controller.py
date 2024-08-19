from typing import List, Dict
from aiohttp import web

from openapi_server.models.pubchem_substances import PubchemSubstances
from openapi_server import util


async def get_substances_using_get(request: web.Request, cid=None, limit=None, page=None, sid=None) -> web.Response:
    """Get pubchem substances

    

    :param cid: cid
    :type cid: List[str]
    :param limit: limit
    :type limit: int
    :param page: page
    :type page: int
    :param sid: sid
    :type sid: List[str]

    """
    return web.Response(status=200)
