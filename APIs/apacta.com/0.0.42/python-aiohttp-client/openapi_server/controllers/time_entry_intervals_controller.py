from typing import List, Dict
from aiohttp import web

from openapi_server.models.time_entry_intervals_get200_response import TimeEntryIntervalsGet200Response
from openapi_server.models.time_entry_intervals_time_entry_interval_id_get200_response import TimeEntryIntervalsTimeEntryIntervalIdGet200Response
from openapi_server import util


async def time_entry_intervals_get(request: web.Request, ) -> web.Response:
    """List possible time entry intervals

    


    """
    return web.Response(status=200)


async def time_entry_intervals_time_entry_interval_id_get(request: web.Request, time_entry_interval_id) -> web.Response:
    """View time entry interval

    

    :param time_entry_interval_id: 
    :type time_entry_interval_id: str
    :type time_entry_interval_id: str

    """
    return web.Response(status=200)
