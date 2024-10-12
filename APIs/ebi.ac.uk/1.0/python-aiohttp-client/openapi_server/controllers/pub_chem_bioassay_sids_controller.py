from typing import List, Dict
from aiohttp import web

from openapi_server.models.bioassays import Bioassays
from openapi_server import util


async def get_bioassays_using_get1(request: web.Request, limit=None, outcome=None, page=None, sids=None) -> web.Response:
    """Get pubchem bioassays associated to particular substance ids (sid) &amp; outcome

    

    :param limit: limit
    :type limit: int
    :param outcome: outcome
    :type outcome: str
    :param page: page
    :type page: int
    :param sids: sids
    :type sids: List[str]

    """
    return web.Response(status=200)
