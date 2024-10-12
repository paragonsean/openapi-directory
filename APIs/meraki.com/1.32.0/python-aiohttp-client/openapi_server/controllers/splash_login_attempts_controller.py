from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_network_splash_login_attempts_1(request: web.Request, network_id, ssid_number=None, login_identifier=None, timespan=None) -> web.Response:
    """List the splash login attempts for a network

    List the splash login attempts for a network

    :param network_id: 
    :type network_id: str
    :param ssid_number: Only return the login attempts for the specified SSID
    :type ssid_number: int
    :param login_identifier: The username, email, or phone number used during login
    :type login_identifier: str
    :param timespan: The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months
    :type timespan: int

    """
    return web.Response(status=200)
