from typing import List, Dict
from aiohttp import web

from openapi_server.models.device_in_past import DeviceInPast
from openapi_server import util


async def meter_values_get(request: web.Request, id, _date) -> web.Response:
    """Gets the Values for a Meter at a given Date.               The first Value found before the given Date is returned.

    Gets the Values for a Meter at a given Date. The first Value found before the given Date is returned.

    :param id: 
    :type id: str
    :param _date: 
    :type _date: str

    """
    _date = util.deserialize_datetime(_date)
    return web.Response(status=200)
