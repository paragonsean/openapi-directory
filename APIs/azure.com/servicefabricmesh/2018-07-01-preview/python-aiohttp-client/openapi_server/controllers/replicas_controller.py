from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_replica_description import ServiceReplicaDescription
from openapi_server.models.service_replica_list import ServiceReplicaList
from openapi_server import util


async def replica_get(request: web.Request, subscription_id, api_version, resource_group_name, application_name, service_name, replica_name) -> web.Response:
    """Gets a specific replica of a given service.

    Gets the information about the specified replica of a given service of an application. The information includes the runtime properties of the replica instance.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_name: The identity of the application.
    :type application_name: str
    :param service_name: The identity of the service.
    :type service_name: str
    :param replica_name: The identity of the service replica.
    :type replica_name: str

    """
    return web.Response(status=200)


async def replica_list_by_service_name(request: web.Request, subscription_id, api_version, resource_group_name, application_name, service_name) -> web.Response:
    """Gets replicas of a given service.

    Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param application_name: The identity of the application.
    :type application_name: str
    :param service_name: The identity of the service.
    :type service_name: str

    """
    return web.Response(status=200)
