from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.media_service import MediaService
from openapi_server.models.media_service_collection import MediaServiceCollection
from openapi_server.models.operation_list_result import OperationListResult
from openapi_server.models.regenerate_key_input import RegenerateKeyInput
from openapi_server.models.regenerate_key_output import RegenerateKeyOutput
from openapi_server.models.service_keys import ServiceKeys
from openapi_server.models.sync_storage_keys_input import SyncStorageKeysInput
from openapi_server import util


async def media_service_check_name_availability(request: web.Request, subscription_id, api_version, parameters) -> web.Response:
    """media_service_check_name_availability

    Checks whether the Media Service resource name is available. The name must be globally unique.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2015-10-01.
    :type api_version: str
    :param parameters: Properties needed to check the availability of a name.
    :type parameters: dict | bytes

    """
    parameters = CheckNameAvailabilityInput.from_dict(parameters)
    return web.Response(status=200)


async def media_service_create(request: web.Request, subscription_id, api_version, resource_group_name, media_service_name, parameters) -> web.Response:
    """media_service_create

    Creates a Media Service.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2015-10-01.
    :type api_version: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param media_service_name: Name of the Media Service.
    :type media_service_name: str
    :param parameters: Media Service properties needed for creation.
    :type parameters: dict | bytes

    """
    parameters = MediaService.from_dict(parameters)
    return web.Response(status=200)


async def media_service_delete(request: web.Request, subscription_id, api_version, resource_group_name, media_service_name) -> web.Response:
    """media_service_delete

    Deletes a Media Service.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2015-10-01.
    :type api_version: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param media_service_name: Name of the Media Service.
    :type media_service_name: str

    """
    return web.Response(status=200)


async def media_service_get(request: web.Request, subscription_id, api_version, resource_group_name, media_service_name) -> web.Response:
    """media_service_get

    Gets a Media Service.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2015-10-01.
    :type api_version: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param media_service_name: Name of the Media Service.
    :type media_service_name: str

    """
    return web.Response(status=200)


async def media_service_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """media_service_list_by_resource_group

    Lists all of the Media Services in a resource group.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2015-10-01.
    :type api_version: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def media_service_list_keys(request: web.Request, subscription_id, api_version, resource_group_name, media_service_name) -> web.Response:
    """media_service_list_keys

    Lists the keys for a Media Service.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2015-10-01.
    :type api_version: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param media_service_name: Name of the Media Service.
    :type media_service_name: str

    """
    return web.Response(status=200)


async def media_service_regenerate_key(request: web.Request, subscription_id, api_version, resource_group_name, media_service_name, parameters) -> web.Response:
    """media_service_regenerate_key

    Regenerates a primary or secondary key for a Media Service.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2015-10-01.
    :type api_version: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param media_service_name: Name of the Media Service.
    :type media_service_name: str
    :param parameters: Properties needed to regenerate the Media Service key.
    :type parameters: dict | bytes

    """
    parameters = RegenerateKeyInput.from_dict(parameters)
    return web.Response(status=200)


async def media_service_sync_storage_keys(request: web.Request, subscription_id, api_version, resource_group_name, media_service_name, parameters) -> web.Response:
    """media_service_sync_storage_keys

    Synchronizes storage account keys for a storage account associated with the Media Service account.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2015-10-01.
    :type api_version: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param media_service_name: Name of the Media Service.
    :type media_service_name: str
    :param parameters: Properties needed to synchronize the keys for a storage account to the Media Service.
    :type parameters: dict | bytes

    """
    parameters = SyncStorageKeysInput.from_dict(parameters)
    return web.Response(status=200)


async def media_service_update(request: web.Request, subscription_id, api_version, resource_group_name, media_service_name, parameters) -> web.Response:
    """media_service_update

    Updates a Media Service.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2015-10-01.
    :type api_version: str
    :param resource_group_name: Name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param media_service_name: Name of the Media Service.
    :type media_service_name: str
    :param parameters: Media Service properties needed for update.
    :type parameters: dict | bytes

    """
    parameters = MediaService.from_dict(parameters)
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Lists all of the available Media Services REST API operations.

    :param api_version: Version of the API to be used with the client request. The current version is 2015-10-01.
    :type api_version: str

    """
    return web.Response(status=200)
