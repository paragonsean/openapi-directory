from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server import util


async def all_activities(request: web.Request, username, start_time=None, end_time=None, limit=None) -> web.Response:
    """All activities for current user

    The Activities endpoint returns information about the user&#39;s activities.

    :param username: a valid username string
    :type username: str
    :param start_time: Start time for filtering, returns records created after given time.
    :type start_time: str
    :param end_time: End time for filtering, returns records created before give time.
    :type end_time: str
    :param limit: Limit the number of records returned.
    :type limit: int

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def destroy_activities(request: web.Request, username) -> web.Response:
    """All activities for current user

    Delete all your activities.

    :param username: a valid username string
    :type username: str

    """
    return web.Response(status=200)


async def get_activity(request: web.Request, username, type, start_time=None, end_time=None, limit=None) -> web.Response:
    """Get activities by type for current user

    The Activities endpoint returns information about the user&#39;s activities.

    :param username: a valid username string
    :type username: str
    :param type: 
    :type type: str
    :param start_time: Start time for filtering, returns records created after given time.
    :type start_time: str
    :param end_time: End time for filtering, returns records created before give time.
    :type end_time: str
    :param limit: Limit the number of records returned.
    :type limit: int

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)
