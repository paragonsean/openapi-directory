from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_group_list import ActionGroupList
from openapi_server.models.action_group_patch_body import ActionGroupPatchBody
from openapi_server.models.action_group_resource import ActionGroupResource
from openapi_server.models.enable_request import EnableRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def action_groups_create_or_update(request: web.Request, resource_group_name, action_group_name, subscription_id, api_version, action_group) -> web.Response:
    """action_groups_create_or_update

    Create a new action group or update an existing one.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param action_group_name: The name of the action group.
    :type action_group_name: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param action_group: The action group to create or use for the update.
    :type action_group: dict | bytes

    """
    action_group = ActionGroupResource.from_dict(action_group)
    return web.Response(status=200)


async def action_groups_delete(request: web.Request, resource_group_name, action_group_name, subscription_id, api_version) -> web.Response:
    """action_groups_delete

    Delete an action group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param action_group_name: The name of the action group.
    :type action_group_name: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def action_groups_enable_receiver(request: web.Request, resource_group_name, action_group_name, subscription_id, api_version, enable_request) -> web.Response:
    """action_groups_enable_receiver

    Enable a receiver in an action group. This changes the receiver&#39;s status from Disabled to Enabled.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param action_group_name: The name of the action group.
    :type action_group_name: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param enable_request: The receiver to re-enable.
    :type enable_request: dict | bytes

    """
    enable_request = EnableRequest.from_dict(enable_request)
    return web.Response(status=200)


async def action_groups_get(request: web.Request, resource_group_name, action_group_name, subscription_id, api_version) -> web.Response:
    """action_groups_get

    Get an action group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param action_group_name: The name of the action group.
    :type action_group_name: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def action_groups_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """action_groups_list_by_resource_group

    Get a list of all action groups in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def action_groups_list_by_subscription_id(request: web.Request, subscription_id, api_version) -> web.Response:
    """action_groups_list_by_subscription_id

    Get a list of all action groups in a subscription.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def action_groups_update(request: web.Request, subscription_id, resource_group_name, action_group_name, api_version, action_group_patch) -> web.Response:
    """action_groups_update

    Updates an existing action group&#39;s tags. To update other fields use the CreateOrUpdate method.

    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param action_group_name: The name of the action group.
    :type action_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param action_group_patch: Parameters supplied to the operation.
    :type action_group_patch: dict | bytes

    """
    action_group_patch = ActionGroupPatchBody.from_dict(action_group_patch)
    return web.Response(status=200)
