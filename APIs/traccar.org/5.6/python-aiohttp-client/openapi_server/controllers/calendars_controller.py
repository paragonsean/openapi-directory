from typing import List, Dict
from aiohttp import web

from openapi_server.models.calendar import Calendar
from openapi_server import util


async def calendars_get(request: web.Request, all=None, user_id=None) -> web.Response:
    """Fetch a list of Calendars

    Without params, it returns a list of Calendars the user has access to

    :param all: Can only be used by admins or managers to fetch all entities
    :type all: bool
    :param user_id: Standard users can use this only with their own _userId_
    :type user_id: int

    """
    return web.Response(status=200)


async def calendars_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Calendar

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def calendars_id_put(request: web.Request, id, body) -> web.Response:
    """Update a Calendar

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Calendar.from_dict(body)
    return web.Response(status=200)


async def calendars_post(request: web.Request, body) -> web.Response:
    """Create a Calendar

    

    :param body: 
    :type body: dict | bytes

    """
    body = Calendar.from_dict(body)
    return web.Response(status=200)
