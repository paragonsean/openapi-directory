from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_appliance_prefixes_delegated_vlan_assignments_3(request: web.Request, serial) -> web.Response:
    """Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

    Return prefixes assigned to all IPv6 enabled VLANs on an appliance.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
