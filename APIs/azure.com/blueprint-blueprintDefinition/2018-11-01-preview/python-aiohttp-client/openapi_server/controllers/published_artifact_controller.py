from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact import Artifact
from openapi_server.models.artifact_list import ArtifactList
from openapi_server import util


async def published_artifacts_get(request: web.Request, api_version, scope, blueprint_name, version_id, artifact_name) -> web.Response:
    """published_artifacts_get

    Get an artifact for a published blueprint definition.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str
    :param version_id: Version of the published blueprint definition.
    :type version_id: str
    :param artifact_name: Name of the blueprint artifact.
    :type artifact_name: str

    """
    return web.Response(status=200)


async def published_artifacts_list(request: web.Request, api_version, scope, blueprint_name, version_id) -> web.Response:
    """published_artifacts_list

    List artifacts for a version of a published blueprint definition.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str
    :param version_id: Version of the published blueprint definition.
    :type version_id: str

    """
    return web.Response(status=200)
