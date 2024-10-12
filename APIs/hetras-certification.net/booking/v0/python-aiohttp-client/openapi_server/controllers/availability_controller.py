from typing import List, Dict
from aiohttp import web

from openapi_server.models.availability_response import AvailabilityResponse
from openapi_server import util


async def availability_get(request: web.Request, app_id, app_key, hotel_id, _from, to, expand=None, skip=None, top=None, inlinecount=None) -> web.Response:
    """Gets the availability and occupancy for a specific hotel and timespan.

    Read past occupancy and future availability for a specific hotel. You can also request the breakdown per room type.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: Specifies the hotel id to request the availability for.
    :type hotel_id: int
    :param _from: Defines the first business day you would like to get availability numbers for.
    :type _from: str
    :param to: Defines the last business day you would like to get availability numbers for. The maximum time span between &lt;i&gt;from&lt;/i&gt;´and &lt;i&gt;to&lt;/i&gt;              is limited to 365 days.
    :type to: str
    :param expand: You can expand the room types breakdown per business day for the availibility numbers if need be.
    :type expand: str
    :param skip: Amount of items to skip.
    :type skip: int
    :param top: Amount of items to select.
    :type top: int
    :param inlinecount: Return total number of items for a given filter criteria.
    :type inlinecount: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
