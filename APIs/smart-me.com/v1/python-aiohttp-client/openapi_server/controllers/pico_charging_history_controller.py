from typing import List, Dict
from aiohttp import web

from openapi_server.models.pico_charging_history_data import PicoChargingHistoryData
from openapi_server import util


async def pico_charging_history_get(request: web.Request, id) -> web.Response:
    """Gets the last charging history for a pico station

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
