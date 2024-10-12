from typing import List, Dict
from aiohttp import web

from openapi_server.models.addons import Addons
from openapi_server import util


async def addons_get(request: web.Request, app_id, app_key, hotel_id, arrival_date, departure_date, channel_code, adults, rooms, room_type, rate_plan_code, expand=None) -> web.Response:
    """Get a list of offers for addon services for the specified guest stay details.

    With the addons request you can get a list of offers for addon services available for a specific rate, room type              and guest stay details.The channel code will define which rates will be returned based on the access control               configuration for related rates.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: Specifies the hotel id to request offers for.
    :type hotel_id: int
    :param arrival_date: Date from when the addon service will be booked to the reservation in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;.
    :type arrival_date: str
    :param departure_date: Date until when the addon service will be booked to the reservation in the ISO-8601 format \&quot;YYYY-MM-DD\&quot;.              This is usually the departure date of the reservation.
    :type departure_date: str
    :param channel_code: Channel Code the rate plan needs to be configured for.
    :type channel_code: str
    :param adults: Number of adults per room.
    :type adults: str
    :param rooms: Number of rooms.
    :type rooms: str
    :param room_type: Only return offers for the specified room type code.
    :type room_type: str
    :param rate_plan_code: Only return offers for the specified rate plan code.
    :type rate_plan_code: str
    :param expand: Expand the rates breakdown if required.
    :type expand: str

    """
    arrival_date = util.deserialize_datetime(arrival_date)
    departure_date = util.deserialize_datetime(departure_date)
    return web.Response(status=200)
