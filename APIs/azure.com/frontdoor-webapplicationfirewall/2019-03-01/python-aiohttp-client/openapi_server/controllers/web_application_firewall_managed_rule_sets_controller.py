from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.managed_rule_set_definition_list import ManagedRuleSetDefinitionList
from openapi_server import util


async def managed_rule_sets_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """managed_rule_sets_list

    Lists all available managed rule sets.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
