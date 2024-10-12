from typing import List, Dict
from aiohttp import web

from openapi_server.models.run_command_input import RunCommandInput
from openapi_server.models.run_command_result import RunCommandResult
from openapi_server import util


async def virtual_machines_run_command(request: web.Request, resource_group_name, vm_name, api_version, subscription_id, parameters) -> web.Response:
    """virtual_machines_run_command

    Run command on the VM.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_name: The name of the virtual machine.
    :type vm_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Run command operation.
    :type parameters: dict | bytes

    """
    parameters = RunCommandInput.from_dict(parameters)
    return web.Response(status=200)
