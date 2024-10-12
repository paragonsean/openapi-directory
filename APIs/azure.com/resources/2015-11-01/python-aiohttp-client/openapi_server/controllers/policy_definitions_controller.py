from typing import List, Dict
from aiohttp import web

from openapi_server.models.policy_definition import PolicyDefinition
from openapi_server import util


async def policy_definitions_create_or_update(request: web.Request, policy_definition_name, api_version, subscription_id, parameters) -> web.Response:
    """policy_definitions_create_or_update

    Create or update policy definition.

    :param policy_definition_name: The policy definition name.
    :type policy_definition_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The policy definition properties
    :type parameters: dict | bytes

    """
    parameters = PolicyDefinition.from_dict(parameters)
    return web.Response(status=200)


async def policy_definitions_delete(request: web.Request, policy_definition_name, api_version, subscription_id) -> web.Response:
    """policy_definitions_delete

    Deletes policy definition.

    :param policy_definition_name: The policy definition name.
    :type policy_definition_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_definitions_get(request: web.Request, policy_definition_name, api_version, subscription_id) -> web.Response:
    """policy_definitions_get

    Gets policy definition.

    :param policy_definition_name: The policy definition name.
    :type policy_definition_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
