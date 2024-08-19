from typing import List, Dict
from aiohttp import web

from openapi_server.models.dedicated_hsm import DedicatedHsm
from openapi_server.models.dedicated_hsm_error import DedicatedHsmError
from openapi_server.models.dedicated_hsm_list_result import DedicatedHsmListResult
from openapi_server.models.dedicated_hsm_patch_parameters import DedicatedHsmPatchParameters
from openapi_server import util


async def dedicated_hsm_create_or_update(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """dedicated_hsm_create_or_update

    Create or Update a dedicated HSM in the specified subscription.

    :param resource_group_name: The name of the Resource Group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the dedicated Hsm
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to create or update the dedicated hsm
    :type parameters: dict | bytes

    """
    parameters = DedicatedHsm.from_dict(parameters)
    return web.Response(status=200)


async def dedicated_hsm_delete(request: web.Request, resource_group_name, name, api_version, subscription_id) -> web.Response:
    """dedicated_hsm_delete

    Deletes the specified Azure Dedicated HSM.

    :param resource_group_name: The name of the Resource Group to which the dedicated HSM belongs.
    :type resource_group_name: str
    :param name: The name of the dedicated HSM to delete
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def dedicated_hsm_get(request: web.Request, resource_group_name, name, api_version, subscription_id) -> web.Response:
    """dedicated_hsm_get

    Gets the specified Azure dedicated HSM.

    :param resource_group_name: The name of the Resource Group to which the dedicated hsm belongs.
    :type resource_group_name: str
    :param name: The name of the dedicated HSM.
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def dedicated_hsm_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id, top=None) -> web.Response:
    """dedicated_hsm_list_by_resource_group

    The List operation gets information about the dedicated hsms associated with the subscription and within the specified resource group.

    :param resource_group_name: The name of the Resource Group to which the dedicated HSM belongs.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Maximum number of results to return.
    :type top: int

    """
    return web.Response(status=200)


async def dedicated_hsm_list_by_subscription(request: web.Request, api_version, subscription_id, top=None) -> web.Response:
    """dedicated_hsm_list_by_subscription

    The List operation gets information about the dedicated HSMs associated with the subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: Maximum number of results to return.
    :type top: int

    """
    return web.Response(status=200)


async def dedicated_hsm_update(request: web.Request, resource_group_name, name, api_version, subscription_id, parameters) -> web.Response:
    """dedicated_hsm_update

    Update a dedicated HSM in the specified subscription.

    :param resource_group_name: The name of the Resource Group to which the server belongs.
    :type resource_group_name: str
    :param name: Name of the dedicated HSM
    :type name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters to patch the dedicated HSM
    :type parameters: dict | bytes

    """
    parameters = DedicatedHsmPatchParameters.from_dict(parameters)
    return web.Response(status=200)
