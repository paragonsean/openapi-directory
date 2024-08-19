from typing import List, Dict
from aiohttp import web

from openapi_server.models.intact_interactions import IntactInteractions
from openapi_server import util


async def get_intact_using_get(request: web.Request, accession=None, confidence=None, gene=None, limit=None, page=None) -> web.Response:
    """Molecular Interactions collected from IntAct

    

    :param accession: accession
    :type accession: List[str]
    :param confidence: confidence
    :type confidence: float
    :param gene: gene
    :type gene: List[str]
    :param limit: limit
    :type limit: int
    :param page: page
    :type page: int

    """
    return web.Response(status=200)
