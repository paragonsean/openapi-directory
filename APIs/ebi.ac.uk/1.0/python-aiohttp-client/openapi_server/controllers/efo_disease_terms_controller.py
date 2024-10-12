from typing import List, Dict
from aiohttp import web

from openapi_server.models.efo_entities import EFOEntities
from openapi_server import util


async def get_efo_using_get(request: web.Request, doid=None, label=None, limit=None, mesh=None, obo_id=None, omim_id=None, page=None, synonym=None) -> web.Response:
    """Get EFO diseases data

    

    :param doid: doid
    :type doid: List[str]
    :param label: label
    :type label: List[str]
    :param limit: limit
    :type limit: int
    :param mesh: mesh
    :type mesh: List[str]
    :param obo_id: oboId
    :type obo_id: List[str]
    :param omim_id: omimId
    :type omim_id: List[str]
    :param page: page
    :type page: int
    :param synonym: synonym
    :type synonym: List[str]

    """
    return web.Response(status=200)
