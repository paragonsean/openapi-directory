from typing import List, Dict
from aiohttp import web

from openapi_server.models.schedule import Schedule
from openapi_server.models.schedules_api_response import SchedulesAPIResponse
from openapi_server import util


async def id_delete_schedules(request: web.Request, id) -> web.Response:
    """Handle DELETE reqeuest for Schedules

    Deletes a schedule with the given id

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_get_schedules(request: web.Request, ) -> web.Response:
    """Handle GET reqeuest for Schedules

    Returns the list of all the schedules saved by the current user


    """
    return web.Response(status=200)


async def id_get_single_schedule(request: web.Request, id) -> web.Response:
    """Handle GET reqeuest for Schedules

    Fetches and returns the schedule with the given id

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_post_schedules(request: web.Request, ) -> web.Response:
    """Handle POST reqeuest for Schedules

    Save schedule using the current provider&#39;s persistence mechanism


    """
    return web.Response(status=200)
