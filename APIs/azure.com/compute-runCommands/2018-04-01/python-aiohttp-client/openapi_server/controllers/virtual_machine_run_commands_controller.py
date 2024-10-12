from typing import List, Dict
from aiohttp import web

from openapi_server.models.run_command_document import RunCommandDocument
from openapi_server.models.run_command_list_result import RunCommandListResult
from openapi_server import util


async def virtual_machine_run_commands_get(request: web.Request, location, command_id, api_version, subscription_id) -> web.Response:
    """virtual_machine_run_commands_get

    Gets specific run command for a subscription in a location.

    :param location: The location upon which run commands is queried.
    :type location: str
    :param command_id: The command id.
    :type command_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_run_commands_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """virtual_machine_run_commands_list

    Lists all available run commands for a subscription in a location.

    :param location: The location upon which run commands is queried.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
