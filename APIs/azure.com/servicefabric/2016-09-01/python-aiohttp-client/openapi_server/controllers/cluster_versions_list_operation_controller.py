from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster_code_versions_list_result import ClusterCodeVersionsListResult
from openapi_server import util


async def cluster_versions_list_by_version(request: web.Request, location, api_version, subscription_id, cluster_version) -> web.Response:
    """cluster_versions_list_by_version

    List cluster code versions by version

    :param location: The location for the cluster code versions, this is different from cluster location
    :type location: str
    :param api_version: The version of the ServiceFabric resource provider api
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param cluster_version: The cluster code version
    :type cluster_version: str

    """
    return web.Response(status=200)
