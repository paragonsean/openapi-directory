from typing import List, Dict
from aiohttp import web

from openapi_server.models.rates import Rates
from openapi_server import util


async def rates_get(request: web.Request, app_id, app_key, hotel_id, arrival_date, departure_date, channel_code, adults, rooms=None, room_type=None, rate_plan_code=None, group_code=None, expand=None) -> web.Response:
    """Get a list of room offers for the specified guest stay details.

    With the rates request you can get a list of different rate offers per room type. You will have to at least               specify the hotel, the arrival and departure date, number of adults per room and the channel code. The channel code              will define which rates will be returned based on the access control configuration for the rates.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: Specifies the hotel id to request offers for.
    :type hotel_id: int
    :param arrival_date: Date of arrival for the guest in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;.
    :type arrival_date: str
    :param departure_date: Date of departure for the guest in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;.
    :type departure_date: str
    :param channel_code: Channel Code the rate plan needs to be configured for.
    :type channel_code: str
    :param adults: Number of adults per room.
    :type adults: str
    :param rooms: Number of rooms (default is 1).
    :type rooms: str
    :param room_type: Only return offers with rates for the specified room type code.
    :type room_type: str
    :param rate_plan_code: Only return offers for the specified room type code.
    :type rate_plan_code: str
    :param group_code: Only return offers for the specified group code.
    :type group_code: str
    :param expand: Expand the rates breakdown if required.
    :type expand: str

    """
    arrival_date = util.deserialize_datetime(arrival_date)
    departure_date = util.deserialize_datetime(departure_date)
    return web.Response(status=200)
