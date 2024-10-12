from typing import List, Dict
from aiohttp import web

from openapi_server.models.agent_registration import AgentRegistration
from openapi_server.models.agent_registration_information_get_default_response import AgentRegistrationInformationGetDefaultResponse
from openapi_server.models.agent_registration_regenerate_key_parameter import AgentRegistrationRegenerateKeyParameter
from openapi_server import util


async def agent_registration_information_get(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """agent_registration_information_get

    Retrieve the automation agent registration information.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def agent_registration_information_regenerate_key(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, parameters) -> web.Response:
    """agent_registration_information_regenerate_key

    Regenerate a primary or secondary agent registration key

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The name of the agent registration key to be regenerated
    :type parameters: dict | bytes

    """
    parameters = AgentRegistrationRegenerateKeyParameter.from_dict(parameters)
    return web.Response(status=200)
