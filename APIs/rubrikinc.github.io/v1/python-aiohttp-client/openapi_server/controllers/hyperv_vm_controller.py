from typing import List, Dict
from aiohttp import web

from openapi_server.models.hyperv_virtual_machine_force_full_request import HypervVirtualMachineForceFullRequest
from openapi_server.models.hyperv_virtual_machine_force_full_response import HypervVirtualMachineForceFullResponse
from openapi_server import util


async def get_hyperv_virtual_machine_force_full_spec(request: web.Request, id) -> web.Response:
    """Retrieve the configuration which has been set for forcing a full snapshot for a Hyper-V Virtual Machine

    Retrieve the configuration created to force a full snapshot for a Hyper-V Virtual Machine.

    :param id: The ID of the Hyper-V virtual machine.
    :type id: str

    """
    return web.Response(status=200)


async def request_hyperv_virtual_machine_force_full_snapshot(request: web.Request, id, body) -> web.Response:
    """Request a full snapshot during next backup job of a Hyper-V virtual machine

    Request a full snapshot during the next backup job of a Hyper-V virtual machine.

    :param id: ID of the Hyper-V virtual machine.
    :type id: str
    :param body: Configuration created to force a full snapshot on the Hyper-V virtual machine.
    :type body: dict | bytes

    """
    body = HypervVirtualMachineForceFullRequest.from_dict(body)
    return web.Response(status=200)
