from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster_code_versions_list_result import ClusterCodeVersionsListResult
from openapi_server import util


async def cluster_versions_get(request: web.Request, location, api_version, subscription_id, cluster_version) -> web.Response:
    """Gets information about a Service Fabric cluster code version available in the specified location.

    Gets information about an available Service Fabric cluster code version.

    :param location: The location for the cluster code versions. This is different from cluster location.
    :type location: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param cluster_version: The cluster code version.
    :type cluster_version: str

    """
    return web.Response(status=200)


async def cluster_versions_get_by_environment(request: web.Request, location, environment, api_version, subscription_id, cluster_version) -> web.Response:
    """Gets information about a Service Fabric cluster code version available for the specified environment.

    Gets information about an available Service Fabric cluster code version by environment.

    :param location: The location for the cluster code versions. This is different from cluster location.
    :type location: str
    :param environment: The operating system of the cluster. The default means all.
    :type environment: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str
    :param cluster_version: The cluster code version.
    :type cluster_version: str

    """
    return web.Response(status=200)


async def cluster_versions_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """Gets the list of Service Fabric cluster code versions available for the specified location.

    Gets all available code versions for Service Fabric cluster resources by location.

    :param location: The location for the cluster code versions. This is different from cluster location.
    :type location: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def cluster_versions_list_by_environment(request: web.Request, location, environment, api_version, subscription_id) -> web.Response:
    """Gets the list of Service Fabric cluster code versions available for the specified environment.

    Gets all available code versions for Service Fabric cluster resources by environment.

    :param location: The location for the cluster code versions. This is different from cluster location.
    :type location: str
    :param environment: The operating system of the cluster. The default means all.
    :type environment: str
    :param api_version: The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification.
    :type api_version: str
    :param subscription_id: The customer subscription identifier.
    :type subscription_id: str

    """
    return web.Response(status=200)
