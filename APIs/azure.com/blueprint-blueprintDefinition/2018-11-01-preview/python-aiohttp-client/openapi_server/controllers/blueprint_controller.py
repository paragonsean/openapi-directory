from typing import List, Dict
from aiohttp import web

from openapi_server.models.blueprint import Blueprint
from openapi_server.models.blueprint_list import BlueprintList
from openapi_server import util


async def blueprints_create_or_update(request: web.Request, api_version, scope, blueprint_name, blueprint) -> web.Response:
    """blueprints_create_or_update

    Create or update a blueprint definition.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str
    :param blueprint: Blueprint definition.
    :type blueprint: dict | bytes

    """
    blueprint = Blueprint.from_dict(blueprint)
    return web.Response(status=200)


async def blueprints_delete(request: web.Request, api_version, scope, blueprint_name) -> web.Response:
    """blueprints_delete

    Delete a blueprint definition.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str

    """
    return web.Response(status=200)


async def blueprints_get(request: web.Request, api_version, scope, blueprint_name) -> web.Response:
    """blueprints_get

    Get a blueprint definition.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str

    """
    return web.Response(status=200)


async def blueprints_list(request: web.Request, api_version, scope) -> web.Response:
    """blueprints_list

    List blueprint definitions.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str

    """
    return web.Response(status=200)
