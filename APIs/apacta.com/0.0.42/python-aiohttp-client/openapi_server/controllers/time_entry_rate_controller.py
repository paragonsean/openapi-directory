from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server import util


async def time_entry_rates_time_entry_rate_id_delete(request: web.Request, time_entry_rate_id) -> web.Response:
    """Delete time entry rate

    

    :param time_entry_rate_id: 
    :type time_entry_rate_id: str
    :type time_entry_rate_id: str

    """
    return web.Response(status=200)
