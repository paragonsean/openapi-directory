from typing import List, Dict
from aiohttp import web

from openapi_server.models.v_meter_to_deactivate import VMeterToDeactivate
from openapi_server import util


async def virtual_billing_meter_deactivate_post(request: web.Request, body) -> web.Response:
    """Beta: Virtual Meter API: Deactivates a Virtual Meter.

    Beta: Virtual Meter API: Deactivates a Virtual Meter.

    :param body: The Meter to activate
    :type body: dict | bytes

    """
    body = VMeterToDeactivate.from_dict(body)
    return web.Response(status=200)
