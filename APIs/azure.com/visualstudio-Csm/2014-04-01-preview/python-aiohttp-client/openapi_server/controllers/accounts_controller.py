from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_resource import AccountResource
from openapi_server.models.account_resource_list_result import AccountResourceListResult
from openapi_server.models.account_resource_request import AccountResourceRequest
from openapi_server.models.account_tag_request import AccountTagRequest
from openapi_server.models.check_name_availability_parameter import CheckNameAvailabilityParameter
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server import util


async def accounts_check_name_availability(request: web.Request, subscription_id, api_version, body) -> web.Response:
    """Accounts_CheckNameAvailability

    Checks if the specified Visual Studio Team Services account name is available. Resource name can be either an account name or an account name and PUID.

    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param body: Parameters describing the name to check availability for.
    :type body: dict | bytes

    """
    body = CheckNameAvailabilityParameter.from_dict(body)
    return web.Response(status=200)


async def accounts_create_or_update(request: web.Request, resource_group_name, subscription_id, api_version, resource_name, body) -> web.Response:
    """Accounts_CreateOrUpdate

    Creates or updates a Visual Studio Team Services account resource.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param resource_name: Name of the resource.
    :type resource_name: str
    :param body: The request data.
    :type body: dict | bytes

    """
    body = AccountResourceRequest.from_dict(body)
    return web.Response(status=200)


async def accounts_delete(request: web.Request, resource_group_name, subscription_id, api_version, resource_name) -> web.Response:
    """Accounts_Delete

    Deletes a Visual Studio Team Services account resource.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param resource_name: Name of the resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def accounts_get(request: web.Request, resource_group_name, subscription_id, api_version, resource_name) -> web.Response:
    """Accounts_Get

    Gets the Visual Studio Team Services account resource details.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param resource_name: Name of the resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def accounts_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Accounts_ListByResourceGroup

    Gets all Visual Studio Team Services account resources under the resource group linked to the specified Azure subscription.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_update(request: web.Request, resource_group_name, subscription_id, api_version, resource_name, body) -> web.Response:
    """Accounts_Update

    Updates tags for Visual Studio Team Services account resource.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param resource_name: Name of the resource.
    :type resource_name: str
    :param body: The request data.
    :type body: dict | bytes

    """
    body = AccountTagRequest.from_dict(body)
    return web.Response(status=200)
