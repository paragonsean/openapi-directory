from typing import List, Dict
from aiohttp import web

from openapi_server.models.targets import Targets
from openapi_server import util


async def get_targets_using_get(request: web.Request, accession=None, limit=None, page=None, target_ids=None) -> web.Response:
    """Get ChEMBL targets

    

    :param accession: accession
    :type accession: List[str]
    :param limit: limit
    :type limit: int
    :param page: page
    :type page: int
    :param target_ids: targetIds
    :type target_ids: List[str]

    """
    return web.Response(status=200)
