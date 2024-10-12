from typing import List, Dict
from aiohttp import web

from openapi_server.models.time_entry_unit_types_get200_response import TimeEntryUnitTypesGet200Response
from openapi_server.models.time_entry_unit_types_time_entry_unit_type_id_get200_response import TimeEntryUnitTypesTimeEntryUnitTypeIdGet200Response
from openapi_server import util


async def time_entry_unit_types_get(request: web.Request, ) -> web.Response:
    """List possible time entry unit types

    


    """
    return web.Response(status=200)


async def time_entry_unit_types_time_entry_unit_type_id_get(request: web.Request, time_entry_unit_type_id) -> web.Response:
    """View time entry unit type

    

    :param time_entry_unit_type_id: 
    :type time_entry_unit_type_id: str
    :type time_entry_unit_type_id: str

    """
    return web.Response(status=200)
