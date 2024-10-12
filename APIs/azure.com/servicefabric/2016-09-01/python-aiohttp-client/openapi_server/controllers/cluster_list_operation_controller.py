from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster_list_result import ClusterListResult
from openapi_server import util


async def clusters_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """clusters_list

    List cluster resource

    :param api_version: The version of the ServiceFabric resource provider api
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str

    """
    return web.Response(status=200)
