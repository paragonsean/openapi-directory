from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def create_alert_get(request: web.Request, who, thing, condition, key) -> web.Response:
    """Create an alert for a thing. A thing must be locked before an alert can be set.

    

    :param who: A comma separated list of Email addresses to send the alert to.
    :type who: str
    :param thing: A unique name of a thing. It is recommended that you use a GUID as to avoid name collisions.
    :type thing: str
    :param condition: A condition that returns a string or a true value if a condition is met.
    :type condition: str
    :param key: A valid key for a locked thing. If the thing is not locked, this can be ignored.
    :type key: str

    """
    return web.Response(status=200)


async def get_alert(request: web.Request, thing, key) -> web.Response:
    """Get the alert attached to a thing.

    

    :param thing: A unique name of a thing.
    :type thing: str
    :param key: A valid key for a locked thing. If the thing is not locked, this can be ignored.
    :type key: str

    """
    return web.Response(status=200)


async def remove_alert(request: web.Request, thing, key) -> web.Response:
    """Remove an alert for a thing.

    

    :param thing: A unique name of a thing.
    :type thing: str
    :param key: A valid key for a locked thing. If the thing is not locked, this can be ignored.
    :type key: str

    """
    return web.Response(status=200)
