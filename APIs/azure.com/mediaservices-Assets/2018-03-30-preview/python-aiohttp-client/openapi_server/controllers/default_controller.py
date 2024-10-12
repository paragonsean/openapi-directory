from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset import Asset
from openapi_server.models.asset_collection import AssetCollection
from openapi_server.models.asset_container_sas import AssetContainerSas
from openapi_server.models.asset_storage_encryption_key import AssetStorageEncryptionKey
from openapi_server.models.assets_list_default_response import AssetsListDefaultResponse
from openapi_server.models.list_container_sas_input import ListContainerSasInput
from openapi_server import util


async def assets_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, asset_name, api_version, parameters) -> web.Response:
    """Create or update an Asset

    Creates or updates an Asset in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param asset_name: The Asset name.
    :type asset_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = Asset.from_dict(parameters)
    return web.Response(status=200)


async def assets_delete(request: web.Request, subscription_id, resource_group_name, account_name, asset_name, api_version) -> web.Response:
    """Delete an Asset.

    Deletes an Asset in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param asset_name: The Asset name.
    :type asset_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def assets_get(request: web.Request, subscription_id, resource_group_name, account_name, asset_name, api_version) -> web.Response:
    """Get an Asset

    Get the details of an Asset in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param asset_name: The Asset name.
    :type asset_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def assets_get_encryption_key(request: web.Request, subscription_id, resource_group_name, account_name, asset_name, api_version) -> web.Response:
    """Gets the Asset storage key

    Gets the Asset storage encryption keys used to decrypt content created by version 2 of the Media Services API

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param asset_name: The Asset name.
    :type asset_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def assets_list(request: web.Request, subscription_id, resource_group_name, account_name, api_version, filter=None, top=None, orderby=None) -> web.Response:
    """List Assets

    List Assets in the Media Services account with optional filtering and ordering

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param filter: Restricts the set of items returned.
    :type filter: str
    :param top: Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    :type top: int
    :param orderby: Specifies the key by which the result collection should be ordered.
    :type orderby: str

    """
    return web.Response(status=200)


async def assets_list_container_sas(request: web.Request, subscription_id, resource_group_name, account_name, asset_name, api_version, parameters) -> web.Response:
    """List the Asset URLs

    Lists storage container URLs with shared access signatures (SAS) for uploading and downloading Asset content. The signatures are derived from the storage account keys.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param asset_name: The Asset name.
    :type asset_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = ListContainerSasInput.from_dict(parameters)
    return web.Response(status=200)


async def assets_update(request: web.Request, subscription_id, resource_group_name, account_name, asset_name, api_version, parameters) -> web.Response:
    """Update an Asset

    Updates an existing Asset in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param asset_name: The Asset name.
    :type asset_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = Asset.from_dict(parameters)
    return web.Response(status=200)
