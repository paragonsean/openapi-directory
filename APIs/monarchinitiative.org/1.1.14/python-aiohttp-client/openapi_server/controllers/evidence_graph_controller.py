from typing import List, Dict
from aiohttp import web

from openapi_server.models.association_results import AssociationResults
from openapi_server.models.graph import Graph
from openapi_server import util


async def get_evidence_graph_object(request: web.Request, id) -> web.Response:
    """Returns evidence graph object for a given association

    Note that every association is assumed to have a unique ID

    :param id: association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada
    :type id: str

    """
    return web.Response(status=200)


async def get_evidence_graph_table(request: web.Request, id, is_publication=None) -> web.Response:
    """Returns evidence as a association_results object given an association

    Note that every association is assumed to have a unique ID

    :param id: association id, e.g. 68e686f6-d05b-46b8-ab1f-1da2fff97ada
    :type id: str
    :param is_publication: If true, considers dc:source as edge
    :type is_publication: bool

    """
    return web.Response(status=200)
