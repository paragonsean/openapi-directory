from typing import List, Dict
from aiohttp import web

from openapi_server.models.time_entry_value_types_get200_response import TimeEntryValueTypesGet200Response
from openapi_server.models.time_entry_value_types_time_entry_value_type_id_get200_response import TimeEntryValueTypesTimeEntryValueTypeIdGet200Response
from openapi_server import util


async def time_entry_value_types_get(request: web.Request, ) -> web.Response:
    """List possible time entry value types

    


    """
    return web.Response(status=200)


async def time_entry_value_types_time_entry_value_type_id_get(request: web.Request, time_entry_value_type_id) -> web.Response:
    """View time entry value type

    

    :param time_entry_value_type_id: 
    :type time_entry_value_type_id: str
    :type time_entry_value_type_id: str

    """
    return web.Response(status=200)
