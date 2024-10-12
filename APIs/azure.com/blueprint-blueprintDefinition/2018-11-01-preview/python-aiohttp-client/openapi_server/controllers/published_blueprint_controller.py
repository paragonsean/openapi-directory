from typing import List, Dict
from aiohttp import web

from openapi_server.models.published_blueprint import PublishedBlueprint
from openapi_server.models.published_blueprint_list import PublishedBlueprintList
from openapi_server import util


async def published_blueprints_create(request: web.Request, api_version, scope, blueprint_name, version_id, published_blueprint=None) -> web.Response:
    """published_blueprints_create

    Publish a new version of the blueprint definition with the latest artifacts. Published blueprint definitions are immutable.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str
    :param version_id: Version of the published blueprint definition.
    :type version_id: str
    :param published_blueprint: Published Blueprint to create or update.
    :type published_blueprint: dict | bytes

    """
    published_blueprint = PublishedBlueprint.from_dict(published_blueprint)
    return web.Response(status=200)


async def published_blueprints_delete(request: web.Request, api_version, scope, blueprint_name, version_id) -> web.Response:
    """published_blueprints_delete

    Delete a published version of a blueprint definition.

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


async def published_blueprints_get(request: web.Request, api_version, scope, blueprint_name, version_id) -> web.Response:
    """published_blueprints_get

    Get a published version of a blueprint definition.

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


async def published_blueprints_list(request: web.Request, api_version, scope, blueprint_name) -> web.Response:
    """published_blueprints_list

    List published versions of given blueprint definition.

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param blueprint_name: Name of the blueprint definition.
    :type blueprint_name: str

    """
    return web.Response(status=200)
