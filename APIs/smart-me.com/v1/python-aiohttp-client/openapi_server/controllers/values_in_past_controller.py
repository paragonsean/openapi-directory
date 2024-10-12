from typing import List, Dict
from aiohttp import web

from openapi_server.models.values_data import ValuesData
from openapi_server import util


async def values_in_past_get(request: web.Request, id, _date) -> web.Response:
    """Gets all (last) values of a device              The first Value found before the given Date is returned.

    Gets the Values for a device at a given Date. The first Value found before the given Date is returned.

    :param id: The ID of the device
    :type id: str
    :param _date: the date of the value
    :type _date: str

    """
    _date = util.deserialize_datetime(_date)
    return web.Response(status=200)
