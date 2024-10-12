from typing import List, Dict
from aiohttp import web

from openapi_server.models.automation import Automation
from openapi_server.models.automation_list import AutomationList
from openapi_server.models.automation_validation_status import AutomationValidationStatus
from openapi_server.models.automations_list_default_response import AutomationsListDefaultResponse
from openapi_server import util


async def automations_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, automation_name, automation) -> web.Response:
    """automations_create_or_update

    Creates or updates a security automation. If a security automation is already created and a subsequent request is issued for the same automation id, then it will be updated.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param automation_name: The security automation name.
    :type automation_name: str
    :param automation: The security automation resource
    :type automation: dict | bytes

    """
    automation = Automation.from_dict(automation)
    return web.Response(status=200)


async def automations_delete(request: web.Request, api_version, subscription_id, resource_group_name, automation_name) -> web.Response:
    """automations_delete

    Deletes a security automation.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param automation_name: The security automation name.
    :type automation_name: str

    """
    return web.Response(status=200)


async def automations_get(request: web.Request, api_version, subscription_id, resource_group_name, automation_name) -> web.Response:
    """automations_get

    Retrieves information about the model of a security automation.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param automation_name: The security automation name.
    :type automation_name: str

    """
    return web.Response(status=200)


async def automations_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """automations_list

    Lists all the security automations in the specified subscription. Use the &#39;nextLink&#39; property in the response to get the next page of security automations for the specified subscription.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str

    """
    return web.Response(status=200)


async def automations_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """automations_list_by_resource_group

    Lists all the security automations in the specified resource group. Use the &#39;nextLink&#39; property in the response to get the next page of security automations for the specified resource group.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def automations_validate(request: web.Request, api_version, subscription_id, resource_group_name, automation_name, automation) -> web.Response:
    """automations_validate

    Validates the security automation model before create or update. Any validation errors are returned to the client.

    :param api_version: API version for the operation
    :type api_version: str
    :param subscription_id: Azure subscription ID
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param automation_name: The security automation name.
    :type automation_name: str
    :param automation: The security automation resource
    :type automation: dict | bytes

    """
    automation = Automation.from_dict(automation)
    return web.Response(status=200)
