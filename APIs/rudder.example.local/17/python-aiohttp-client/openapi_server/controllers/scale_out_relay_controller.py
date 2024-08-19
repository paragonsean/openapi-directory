from typing import List, Dict
from aiohttp import web

from openapi_server.models.demote_to_node200_response import DemoteToNode200Response
from openapi_server.models.promote_to_relay200_response import PromoteToRelay200Response
from openapi_server import util


async def demote_to_node(request: web.Request, node_id) -> web.Response:
    """Demote a relay to simple node

    Demote a relay to a simple node.

    :param node_id: Id of the target node
    :type node_id: str

    """
    return web.Response(status=200)


async def promote_to_relay(request: web.Request, node_id) -> web.Response:
    """Promote a node to relay

    Promote a node to relay

    :param node_id: Id of the target node
    :type node_id: str

    """
    return web.Response(status=200)
