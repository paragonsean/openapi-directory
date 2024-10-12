from typing import List, Dict
from aiohttp import web

from openapi_server.models.who_is_blueprint_contract import WhoIsBlueprintContract
from openapi_server import util


async def assignments_who_is_blueprint(request: web.Request, api_version, scope, assignment_name) -> web.Response:
    """assignments_who_is_blueprint

    Get Blueprints service SPN objectId

    :param api_version: Client API Version.
    :type api_version: str
    :param scope: The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use.
    :type scope: str
    :param assignment_name: Name of the blueprint assignment.
    :type assignment_name: str

    """
    return web.Response(status=200)
