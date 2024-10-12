from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact import Artifact
from openapi_server.models.artifact_list import ArtifactList
from openapi_server import util


async def published_artifacts_get(request: web.Request, api_version, management_group_name, blueprint_name, version_id, artifact_name) -> web.Response:
    """published_artifacts_get

    Get an artifact for a published Blueprint.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str
    :param blueprint_name: name of the blueprint.
    :type blueprint_name: str
    :param version_id: version of the published blueprint.
    :type version_id: str
    :param artifact_name: name of the artifact.
    :type artifact_name: str

    """
    return web.Response(status=200)


async def published_artifacts_list(request: web.Request, api_version, management_group_name, blueprint_name, version_id) -> web.Response:
    """published_artifacts_list

    List artifacts for a published Blueprint.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str
    :param blueprint_name: name of the blueprint.
    :type blueprint_name: str
    :param version_id: version of the published blueprint.
    :type version_id: str

    """
    return web.Response(status=200)
