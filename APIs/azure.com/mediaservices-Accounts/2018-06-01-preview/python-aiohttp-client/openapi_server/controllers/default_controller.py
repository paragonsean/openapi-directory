from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.entity_name_availability_check_output import EntityNameAvailabilityCheckOutput
from openapi_server.models.media_service import MediaService
from openapi_server.models.media_service_collection import MediaServiceCollection
from openapi_server.models.operation_collection import OperationCollection
from openapi_server.models.subscription_media_service import SubscriptionMediaService
from openapi_server.models.subscription_media_service_collection import SubscriptionMediaServiceCollection
from openapi_server.models.sync_storage_keys_input import SyncStorageKeysInput
from openapi_server import util


async def locations_check_name_availability(request: web.Request, subscription_id, location_name, api_version, parameters) -> web.Response:
    """Check Name Availability

    Checks whether the Media Service resource name is available.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param location_name: 
    :type location_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = CheckNameAvailabilityInput.from_dict(parameters)
    return web.Response(status=200)


async def mediaservices_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, parameters) -> web.Response:
    """Create or update a Media Services account

    Creates or updates a Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = MediaService.from_dict(parameters)
    return web.Response(status=200)


async def mediaservices_delete(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """Delete a Media Services account.

    Deletes a Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def mediaservices_get(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """Get a Media Services account

    Get the details of a Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def mediaservices_get_by_subscription(request: web.Request, subscription_id, account_name, api_version) -> web.Response:
    """Get a Media Services account

    Get the details of a Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def mediaservices_list(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """List Media Services accounts

    List Media Services accounts in the resource group

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def mediaservices_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """List Media Services accounts

    List Media Services accounts in the subscription.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def mediaservices_sync_storage_keys(request: web.Request, subscription_id, resource_group_name, account_name, api_version, parameters) -> web.Response:
    """Synchronizes Storage Account Keys

    Synchronizes storage account keys for a storage account associated with the Media Service account.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = SyncStorageKeysInput.from_dict(parameters)
    return web.Response(status=200)


async def mediaservices_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, parameters) -> web.Response:
    """Update a Media Services account

    Updates an existing Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = MediaService.from_dict(parameters)
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version) -> web.Response:
    """List Operations

    Lists all the Media Services operations.

    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
