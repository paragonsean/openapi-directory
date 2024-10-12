from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster_code_versions_list_result import ClusterCodeVersionsListResult
from openapi_server.models.cluster_code_versions_result import ClusterCodeVersionsResult
from openapi_server import util


async def cluster_versions_get(request: web.Request, location, environment, api_version, subscription_id, cluster_version) -> web.Response:
    """cluster_versions_get

    Get cluster code versions by environment and version

    :param location: The location for the cluster code versions, this is different from cluster location
    :type location: str
    :param environment: Cluster operating system, the default means all
    :type environment: str
    :param api_version: The version of the ServiceFabric resource provider api
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param cluster_version: The cluster code version
    :type cluster_version: str

    """
    return web.Response(status=200)


async def cluster_versions_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """cluster_versions_list

    List cluster code versions by location

    :param location: The location for the cluster code versions, this is different from cluster location
    :type location: str
    :param api_version: The version of the ServiceFabric resource provider api
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str

    """
    return web.Response(status=200)


async def cluster_versions_list_by_environment(request: web.Request, location, environment, api_version, subscription_id) -> web.Response:
    """cluster_versions_list_by_environment

    List cluster code versions by environment

    :param location: The location for the cluster code versions, this is different from cluster location
    :type location: str
    :param environment: Cluster operating system, the default means all
    :type environment: str
    :param api_version: The version of the ServiceFabric resource provider api
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str

    """
    return web.Response(status=200)
