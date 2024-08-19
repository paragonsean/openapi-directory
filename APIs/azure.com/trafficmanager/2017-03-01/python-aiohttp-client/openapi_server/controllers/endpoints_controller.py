from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.delete_operation_result import DeleteOperationResult
from openapi_server.models.endpoint import Endpoint
from openapi_server import util


async def endpoints_create_or_update(request: web.Request, resource_group_name, profile_name, endpoint_type, endpoint_name, api_version, subscription_id, parameters) -> web.Response:
    """endpoints_create_or_update

    Create or update a Traffic Manager endpoint.

    :param resource_group_name: The name of the resource group containing the Traffic Manager endpoint to be created or updated.
    :type resource_group_name: str
    :param profile_name: The name of the Traffic Manager profile.
    :type profile_name: str
    :param endpoint_type: The type of the Traffic Manager endpoint to be created or updated.
    :type endpoint_type: str
    :param endpoint_name: The name of the Traffic Manager endpoint to be created or updated.
    :type endpoint_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The Traffic Manager endpoint parameters supplied to the CreateOrUpdate operation.
    :type parameters: dict | bytes

    """
    parameters = Endpoint.from_dict(parameters)
    return web.Response(status=200)


async def endpoints_delete(request: web.Request, resource_group_name, profile_name, endpoint_type, endpoint_name, api_version, subscription_id) -> web.Response:
    """endpoints_delete

    Deletes a Traffic Manager endpoint.

    :param resource_group_name: The name of the resource group containing the Traffic Manager endpoint to be deleted.
    :type resource_group_name: str
    :param profile_name: The name of the Traffic Manager profile.
    :type profile_name: str
    :param endpoint_type: The type of the Traffic Manager endpoint to be deleted.
    :type endpoint_type: str
    :param endpoint_name: The name of the Traffic Manager endpoint to be deleted.
    :type endpoint_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def endpoints_get(request: web.Request, resource_group_name, profile_name, endpoint_type, endpoint_name, api_version, subscription_id) -> web.Response:
    """endpoints_get

    Gets a Traffic Manager endpoint.

    :param resource_group_name: The name of the resource group containing the Traffic Manager endpoint.
    :type resource_group_name: str
    :param profile_name: The name of the Traffic Manager profile.
    :type profile_name: str
    :param endpoint_type: The type of the Traffic Manager endpoint.
    :type endpoint_type: str
    :param endpoint_name: The name of the Traffic Manager endpoint.
    :type endpoint_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def endpoints_update(request: web.Request, resource_group_name, profile_name, endpoint_type, endpoint_name, api_version, subscription_id, parameters) -> web.Response:
    """endpoints_update

    Update a Traffic Manager endpoint.

    :param resource_group_name: The name of the resource group containing the Traffic Manager endpoint to be updated.
    :type resource_group_name: str
    :param profile_name: The name of the Traffic Manager profile.
    :type profile_name: str
    :param endpoint_type: The type of the Traffic Manager endpoint to be updated.
    :type endpoint_type: str
    :param endpoint_name: The name of the Traffic Manager endpoint to be updated.
    :type endpoint_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The Traffic Manager endpoint parameters supplied to the Update operation.
    :type parameters: dict | bytes

    """
    parameters = Endpoint.from_dict(parameters)
    return web.Response(status=200)
