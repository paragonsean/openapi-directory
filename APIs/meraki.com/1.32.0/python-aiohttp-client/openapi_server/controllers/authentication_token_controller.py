from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_device_appliance_vmx_authentication_token201_response import CreateDeviceApplianceVmxAuthenticationToken201Response
from openapi_server import util


async def create_device_appliance_vmx_authentication_token_2(request: web.Request, serial) -> web.Response:
    """Generate a new vMX authentication token

    Generate a new vMX authentication token

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
