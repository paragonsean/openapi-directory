from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_source import ArtifactSource
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.response_with_continuation_artifact_source import ResponseWithContinuationArtifactSource
from openapi_server import util


async def artifact_source_create_or_update_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, artifact_source) -> web.Response:
    """artifact_source_create_or_update_resource

    Create or replace an existing artifact source.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the artifact source.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param artifact_source: 
    :type artifact_source: dict | bytes

    """
    artifact_source = ArtifactSource.from_dict(artifact_source)
    return web.Response(status=200)


async def artifact_source_delete_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """artifact_source_delete_resource

    Delete artifact source.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the artifact source.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def artifact_source_get_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """artifact_source_get_resource

    Get artifact source.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the artifact source.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def artifact_source_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, filter=None, top=None, order_by=None) -> web.Response:
    """artifact_source_list

    List artifact sources.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param order_by: 
    :type order_by: str

    """
    return web.Response(status=200)


async def artifact_source_patch_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, artifact_source) -> web.Response:
    """artifact_source_patch_resource

    Modify properties of artifact sources.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the artifact source.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param artifact_source: 
    :type artifact_source: dict | bytes

    """
    artifact_source = ArtifactSource.from_dict(artifact_source)
    return web.Response(status=200)
