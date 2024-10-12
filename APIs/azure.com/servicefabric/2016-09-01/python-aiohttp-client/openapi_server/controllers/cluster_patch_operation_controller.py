from typing import List, Dict
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_update_parameters import ClusterUpdateParameters
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def clusters_update(request: web.Request, resource_group_name, cluster_name, api_version, subscription_id, parameters) -> web.Response:
    """clusters_update

    Update cluster configuration

    :param resource_group_name: The name of the resource group to which the resource belongs or get created
    :type resource_group_name: str
    :param cluster_name: The name of the cluster resource
    :type cluster_name: str
    :param api_version: The version of the ServiceFabric resource provider api
    :type api_version: str
    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param parameters: The parameters which contains the property value and property name which used to update the cluster configuration
    :type parameters: dict | bytes

    """
    parameters = ClusterUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
