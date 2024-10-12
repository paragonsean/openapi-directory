from typing import List, Dict
from aiohttp import web

from openapi_server.models.m_bus_data import MBusData
from openapi_server import util


async def m_bus_post(request: web.Request, body) -> web.Response:
    """M-BUS API: Adds data of a M-BUS Meter to the smart-me Cloud.              Just send us the M-BUS Telegram (RSP_UD) and we will do the Rest.

    M-BUS API: Adds data of a M-BUS Meter to the smart-me Cloud.              Just send us the M-BUS Telegram (RSP_UD) and we will do the Rest.

    :param body: The M-BUS Telegram
    :type body: dict | bytes

    """
    body = MBusData.from_dict(body)
    return web.Response(status=200)
