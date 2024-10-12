from typing import List, Dict
from aiohttp import web

from openapi_server.models.run_command_input import RunCommandInput
from openapi_server.models.run_command_result import RunCommandResult
from openapi_server import util


async def virtual_machine_scale_set_vms_run_command(request: web.Request, resource_group_name, vm_scale_set_name, instance_id, api_version, subscription_id, parameters) -> web.Response:
    """virtual_machine_scale_set_vms_run_command

    Run command on a virtual machine in a VM scale set.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param vm_scale_set_name: The name of the VM scale set.
    :type vm_scale_set_name: str
    :param instance_id: The instance ID of the virtual machine.
    :type instance_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Run command operation.
    :type parameters: dict | bytes

    """
    parameters = RunCommandInput.from_dict(parameters)
    return web.Response(status=200)
