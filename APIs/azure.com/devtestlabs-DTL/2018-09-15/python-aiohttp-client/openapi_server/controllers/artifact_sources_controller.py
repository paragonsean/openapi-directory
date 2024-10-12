from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact_source import ArtifactSource
from openapi_server.models.artifact_source_fragment import ArtifactSourceFragment
from openapi_server.models.artifact_source_list import ArtifactSourceList
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def artifact_sources_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, artifact_source) -> web.Response:
    """artifact_sources_create_or_update

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
    :param artifact_source: Properties of an artifact source.
    :type artifact_source: dict | bytes

    """
    artifact_source = ArtifactSource.from_dict(artifact_source)
    return web.Response(status=200)


async def artifact_sources_delete(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """artifact_sources_delete

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


async def artifact_sources_get(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, expand=None) -> web.Response:
    """artifact_sources_get

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
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;displayName)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def artifact_sources_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """artifact_sources_list

    List artifact sources in a given lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;displayName)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;)
    :type filter: str
    :param top: The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39;
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39;
    :type orderby: str

    """
    return web.Response(status=200)


async def artifact_sources_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, artifact_source) -> web.Response:
    """artifact_sources_update

    Allows modifying tags of artifact sources. All other properties will be ignored.

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
    :param artifact_source: Properties of an artifact source.
    :type artifact_source: dict | bytes

    """
    artifact_source = ArtifactSourceFragment.from_dict(artifact_source)
    return web.Response(status=200)
