from typing import List, Dict
from aiohttp import web

from openapi_server.models.extension_resource import ExtensionResource
from openapi_server.models.extension_resource_list_result import ExtensionResourceListResult
from openapi_server.models.extension_resource_request import ExtensionResourceRequest
from openapi_server import util


async def extensions_create(request: web.Request, resource_group_name, subscription_id, api_version, account_resource_name, extension_resource_name, body) -> web.Response:
    """Extensions_Create

    Registers the extension with a Visual Studio Team Services account.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param account_resource_name: The name of the Visual Studio Team Services account resource.
    :type account_resource_name: str
    :param extension_resource_name: The name of the extension.
    :type extension_resource_name: str
    :param body: An object containing additional information related to the extension request.
    :type body: dict | bytes

    """
    body = ExtensionResourceRequest.from_dict(body)
    return web.Response(status=200)


async def extensions_delete(request: web.Request, resource_group_name, subscription_id, api_version, account_resource_name, extension_resource_name) -> web.Response:
    """Extensions_Delete

    Removes an extension resource registration for a Visual Studio Team Services account.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param account_resource_name: The name of the Visual Studio Team Services account resource.
    :type account_resource_name: str
    :param extension_resource_name: The name of the extension.
    :type extension_resource_name: str

    """
    return web.Response(status=200)


async def extensions_get(request: web.Request, resource_group_name, subscription_id, api_version, account_resource_name, extension_resource_name) -> web.Response:
    """Extensions_Get

    Gets the details of an extension associated with a Visual Studio Team Services account resource.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param account_resource_name: The name of the Visual Studio Team Services account resource.
    :type account_resource_name: str
    :param extension_resource_name: The name of the extension.
    :type extension_resource_name: str

    """
    return web.Response(status=200)


async def extensions_list_by_account(request: web.Request, resource_group_name, subscription_id, api_version, account_resource_name) -> web.Response:
    """Extensions_ListByAccount

    Gets the details of the extension resources created within the resource group.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param account_resource_name: The name of the Visual Studio Team Services account resource.
    :type account_resource_name: str

    """
    return web.Response(status=200)


async def extensions_update(request: web.Request, resource_group_name, subscription_id, api_version, account_resource_name, extension_resource_name, body) -> web.Response:
    """Extensions_Update

    Updates an existing extension registration for the Visual Studio Team Services account.

    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param subscription_id: The Azure subscription identifier.
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param account_resource_name: The name of the Visual Studio Team Services account resource.
    :type account_resource_name: str
    :param extension_resource_name: The name of the extension.
    :type extension_resource_name: str
    :param body: An object containing additional information related to the extension request.
    :type body: dict | bytes

    """
    body = ExtensionResourceRequest.from_dict(body)
    return web.Response(status=200)
