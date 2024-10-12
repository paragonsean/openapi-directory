from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_rp_manifest import CustomRPManifest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.list_by_custom_rp_manifest import ListByCustomRPManifest
from openapi_server.models.resource_providers_update import ResourceProvidersUpdate
from openapi_server import util


async def custom_resource_provider_create_or_update(request: web.Request, subscription_id, resource_group_name, resource_provider_name, api_version, resource_provider) -> web.Response:
    """custom_resource_provider_create_or_update

    Creates or updates the custom resource provider.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_provider_name: The name of the resource provider.
    :type resource_provider_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param resource_provider: The parameters required to create or update a custom resource provider definition.
    :type resource_provider: dict | bytes

    """
    resource_provider = CustomRPManifest.from_dict(resource_provider)
    return web.Response(status=200)


async def custom_resource_provider_delete(request: web.Request, subscription_id, resource_group_name, resource_provider_name, api_version) -> web.Response:
    """custom_resource_provider_delete

    Deletes the custom resource provider.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_provider_name: The name of the resource provider.
    :type resource_provider_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def custom_resource_provider_get(request: web.Request, subscription_id, resource_group_name, resource_provider_name, api_version) -> web.Response:
    """custom_resource_provider_get

    Gets the custom resource provider manifest.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_provider_name: The name of the resource provider.
    :type resource_provider_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def custom_resource_provider_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """custom_resource_provider_list_by_resource_group

    Gets all the custom resource providers within a resource group.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def custom_resource_provider_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """custom_resource_provider_list_by_subscription

    Gets all the custom resource providers within a subscription.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str

    """
    return web.Response(status=200)


async def custom_resource_provider_update(request: web.Request, subscription_id, resource_group_name, resource_provider_name, api_version, patchable_resource) -> web.Response:
    """custom_resource_provider_update

    Updates an existing custom resource provider. The only value that can be updated via PATCH currently is the tags.

    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000)
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_provider_name: The name of the resource provider.
    :type resource_provider_name: str
    :param api_version: The API version to be used with the HTTP request.
    :type api_version: str
    :param patchable_resource: The updatable fields of a custom resource provider.
    :type patchable_resource: dict | bytes

    """
    patchable_resource = ResourceProvidersUpdate.from_dict(patchable_resource)
    return web.Response(status=200)
