from typing import List, Dict
from aiohttp import web

from openapi_server.models.blueprint import Blueprint
from openapi_server.models.blueprint_list import BlueprintList
from openapi_server import util


async def blueprints_create_or_update(request: web.Request, api_version, management_group_name, blueprint_name, blueprint) -> web.Response:
    """blueprints_create_or_update

    Create or update Blueprint definition.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str
    :param blueprint_name: name of the blueprint.
    :type blueprint_name: str
    :param blueprint: Blueprint definition.
    :type blueprint: dict | bytes

    """
    blueprint = Blueprint.from_dict(blueprint)
    return web.Response(status=200)


async def blueprints_delete(request: web.Request, api_version, management_group_name, blueprint_name) -> web.Response:
    """blueprints_delete

    Delete a blueprint definition.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str
    :param blueprint_name: name of the blueprint.
    :type blueprint_name: str

    """
    return web.Response(status=200)


async def blueprints_get(request: web.Request, api_version, management_group_name, blueprint_name) -> web.Response:
    """blueprints_get

    Get a blueprint definition.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str
    :param blueprint_name: name of the blueprint.
    :type blueprint_name: str

    """
    return web.Response(status=200)


async def blueprints_list(request: web.Request, api_version, management_group_name) -> web.Response:
    """blueprints_list

    List Blueprint definitions within a Management Group.

    :param api_version: Client Api Version.
    :type api_version: str
    :param management_group_name: ManagementGroup where blueprint stores.
    :type management_group_name: str

    """
    return web.Response(status=200)
