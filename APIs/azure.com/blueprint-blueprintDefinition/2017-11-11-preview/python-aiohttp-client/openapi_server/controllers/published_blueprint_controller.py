from typing import List, Dict
from aiohttp import web

from openapi_server.models.published_blueprint import PublishedBlueprint
from openapi_server.models.published_blueprint_list import PublishedBlueprintList
from openapi_server import util


async def published_blueprints_create(request: web.Request, api_version, management_group_name, blueprint_name, version_id) -> web.Response:
    """published_blueprints_create

    Publish a new version of the Blueprint with the latest artifacts. Published Blueprints are immutable.

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


async def published_blueprints_delete(request: web.Request, api_version, management_group_name, blueprint_name, version_id) -> web.Response:
    """published_blueprints_delete

    Delete a published Blueprint.

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


async def published_blueprints_get(request: web.Request, api_version, management_group_name, blueprint_name, version_id) -> web.Response:
    """published_blueprints_get

    Get a published Blueprint.

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


async def published_blueprints_list(request: web.Request, api_version, management_group_name, blueprint_name) -> web.Response:
    """published_blueprints_list

    List published versions of given Blueprint.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str
    :param blueprint_name: name of the blueprint.
    :type blueprint_name: str

    """
    return web.Response(status=200)
