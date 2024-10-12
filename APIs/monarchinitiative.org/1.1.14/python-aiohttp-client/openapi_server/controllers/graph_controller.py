from typing import List, Dict
from aiohttp import web

from openapi_server.models.bio_object import BioObject
from openapi_server.models.graph import Graph
from openapi_server import util


async def get_edge_resource(request: web.Request, id, depth=None, direction=None, relationship_type=None, entail=None, graph=None) -> web.Response:
    """Returns edges emanating from a given node

    

    :param id: CURIE e.g. HP:0000465
    :type id: str
    :param depth: How far to traverse for neighbors
    :type depth: int
    :param direction: Which direction to traverse (used only if relationship_type is defined)
    :type direction: str
    :param relationship_type: Relationship type to traverse
    :type relationship_type: List[str]
    :param entail: Include sub-properties and equivalent properties
    :type entail: bool
    :param graph: Which monarch graph to query
    :type graph: str

    """
    return web.Response(status=200)


async def get_node_resource(request: web.Request, id) -> web.Response:
    """Returns a graph node

    A node is an abstract representation of some kind of entity. The entity may be a physical thing such as a patient, a molecular entity such as a gene or protein, or a conceptual entity such as a class from an ontology.

    :param id: CURIE e.g. HP:0000465
    :type id: str

    """
    return web.Response(status=200)
