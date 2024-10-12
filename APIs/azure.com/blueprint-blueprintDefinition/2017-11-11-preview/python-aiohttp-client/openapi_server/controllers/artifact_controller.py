from typing import List, Dict
from aiohttp import web

from openapi_server.models.artifact import Artifact
from openapi_server.models.artifact_list import ArtifactList
from openapi_server import util


async def artifacts_create_or_update(request: web.Request, api_version, management_group_name, blueprint_name, artifact_name, artifact) -> web.Response:
    """artifacts_create_or_update

    Create or update Blueprint artifact.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str
    :param blueprint_name: name of the blueprint.
    :type blueprint_name: str
    :param artifact_name: name of the artifact.
    :type artifact_name: str
    :param artifact: Blueprint artifact to save.
    :type artifact: dict | bytes

    """
    artifact = Artifact.from_dict(artifact)
    return web.Response(status=200)


async def artifacts_delete(request: web.Request, api_version, management_group_name, blueprint_name, artifact_name) -> web.Response:
    """artifacts_delete

    Delete a Blueprint artifact.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str
    :param blueprint_name: name of the blueprint.
    :type blueprint_name: str
    :param artifact_name: name of the artifact.
    :type artifact_name: str

    """
    return web.Response(status=200)


async def artifacts_get(request: web.Request, api_version, management_group_name, blueprint_name, artifact_name) -> web.Response:
    """artifacts_get

    Get a Blueprint artifact.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str
    :param blueprint_name: name of the blueprint.
    :type blueprint_name: str
    :param artifact_name: name of the artifact.
    :type artifact_name: str

    """
    return web.Response(status=200)


async def artifacts_list(request: web.Request, api_version, management_group_name, blueprint_name) -> web.Response:
    """artifacts_list

    List artifacts for a given Blueprint.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str
    :param blueprint_name: name of the blueprint.
    :type blueprint_name: str

    """
    return web.Response(status=200)
