from typing import List, Dict
from aiohttp import web

from openapi_server.models.maps_list_operations_default_response import MapsListOperationsDefaultResponse
from openapi_server.models.private_atlas import PrivateAtlas
from openapi_server.models.private_atlas_create_parameters import PrivateAtlasCreateParameters
from openapi_server.models.private_atlas_list import PrivateAtlasList
from openapi_server.models.private_atlas_update_parameters import PrivateAtlasUpdateParameters
from openapi_server import util


async def private_atlases_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, private_atlas_name, private_atlas_create_parameters) -> web.Response:
    """private_atlases_create_or_update

    Create or update a Private Atlas resource. Private Atlas resource will enable the usage of Azure resources to build a custom set of mapping data. It requires an account to exist before it can be created.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str
    :param private_atlas_name: The name of the Private Atlas instance.
    :type private_atlas_name: str
    :param private_atlas_create_parameters: The new or updated parameters for the Private Atlas resource.
    :type private_atlas_create_parameters: dict | bytes

    """
    private_atlas_create_parameters = PrivateAtlasCreateParameters.from_dict(private_atlas_create_parameters)
    return web.Response(status=200)


async def private_atlases_delete(request: web.Request, api_version, subscription_id, resource_group_name, account_name, private_atlas_name) -> web.Response:
    """private_atlases_delete

    Delete a Private Atlas resource.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str
    :param private_atlas_name: The name of the Private Atlas instance.
    :type private_atlas_name: str

    """
    return web.Response(status=200)


async def private_atlases_get(request: web.Request, api_version, subscription_id, resource_group_name, account_name, private_atlas_name) -> web.Response:
    """private_atlases_get

    Get a Private Atlas resource.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str
    :param private_atlas_name: The name of the Private Atlas instance.
    :type private_atlas_name: str

    """
    return web.Response(status=200)


async def private_atlases_list_by_account(request: web.Request, api_version, subscription_id, resource_group_name, account_name) -> web.Response:
    """private_atlases_list_by_account

    Get all Private Atlas instances for an Azure Map Account

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str

    """
    return web.Response(status=200)


async def private_atlases_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, private_atlas_name, private_atlas_update_parameters) -> web.Response:
    """private_atlases_update

    Updates the Private Atlas resource. Only a subset of the parameters may be updated after creation, such as Tags.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str
    :param private_atlas_name: The name of the Private Atlas instance.
    :type private_atlas_name: str
    :param private_atlas_update_parameters: The updated parameters for the Private Atlas.
    :type private_atlas_update_parameters: dict | bytes

    """
    private_atlas_update_parameters = PrivateAtlasUpdateParameters.from_dict(private_atlas_update_parameters)
    return web.Response(status=200)
