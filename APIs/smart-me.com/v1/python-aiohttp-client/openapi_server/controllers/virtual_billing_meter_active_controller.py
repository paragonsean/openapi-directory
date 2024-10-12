from typing import List, Dict
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server.models.v_meter_to_activate import VMeterToActivate
from openapi_server import util


async def virtual_billing_meter_active_get(request: web.Request, ) -> web.Response:
    """Beta: Gets all active virtual meters

    Beta: Gets all active virtual meters.


    """
    return web.Response(status=200)


async def virtual_billing_meter_active_post(request: web.Request, body) -> web.Response:
    """Beta: Virtual Meter API: Activates a Meter and add the Consumption to a Virtual Meter assosiated with the User.

    Beta: Virtual Meter API: Activates a Meter and add the Consumption to a Virtual Meter assosiated with the User.

    :param body: The Meter to activate
    :type body: dict | bytes

    """
    body = VMeterToActivate.from_dict(body)
    return web.Response(status=200)
