from typing import List, Dict
from aiohttp import web

from openapi_server.models.node import Node
from openapi_server.models.node_list_result import NodeListResult
from openapi_server import util


async def get_node(request: web.Request, id) -> web.Response:
    """Show node details

    Get details of infrastructure nodes. Only admin users can get this information. The proxy id is required for adding a data source for selecting appropriate proxy node to add the data source.

    :param id: entity id
    :type id: str

    """
    return web.Response(status=200)


async def list_nodes(request: web.Request, ) -> web.Response:
    """List nodes

    Get list of infrastructure nodes. Only admin users can retrieve this information.


    """
    return web.Response(status=200)
