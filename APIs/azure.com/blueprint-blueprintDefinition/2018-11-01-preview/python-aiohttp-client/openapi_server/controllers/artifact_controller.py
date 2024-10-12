from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact import Artifact
from openapi_server.models.artifact_list import ArtifactList
from openapi_server import util


async def artifacts_create_or_update(request: web.Request, api_version, scope, blueprint_name, artifact_name, artifact) -> web.Response:
    """artifacts_create_or_update

    Create or update blueprint artifact.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str
    :param artifact_name: Name of the blueprint artifact.
    :type artifact_name: str
    :param artifact: Blueprint artifact to create or update.
    :type artifact: dict | bytes

    """
    artifact = Artifact.from_dict(artifact)
    return web.Response(status=200)


async def artifacts_delete(request: web.Request, api_version, scope, blueprint_name, artifact_name) -> web.Response:
    """artifacts_delete

    Delete a blueprint artifact.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str
    :param artifact_name: Name of the blueprint artifact.
    :type artifact_name: str

    """
    return web.Response(status=200)


async def artifacts_get(request: web.Request, api_version, scope, blueprint_name, artifact_name) -> web.Response:
    """artifacts_get

    Get a blueprint artifact.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str
    :param artifact_name: Name of the blueprint artifact.
    :type artifact_name: str

    """
    return web.Response(status=200)


async def artifacts_list(request: web.Request, api_version, scope, blueprint_name) -> web.Response:
    """artifacts_list

    List artifacts for a given blueprint definition.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str

    """
    return web.Response(status=200)
