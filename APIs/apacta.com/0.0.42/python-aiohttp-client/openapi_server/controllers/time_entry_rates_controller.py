from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.time_entries_post_request import TimeEntriesPostRequest
from openapi_server.models.time_entry_rates_get200_response import TimeEntryRatesGet200Response
from openapi_server.models.time_entry_rates_time_entry_rate_id_get200_response import TimeEntryRatesTimeEntryRateIdGet200Response
from openapi_server import util


async def time_entry_rates_get(request: web.Request, ) -> web.Response:
    """List time entry rates

    


    """
    return web.Response(status=200)


async def time_entry_rates_post(request: web.Request, body=None) -> web.Response:
    """Add new time entry rate

    

    :param body: 
    :type body: dict | bytes

    """
    body = TimeEntriesPostRequest.from_dict(body)
    return web.Response(status=200)


async def time_entry_rates_time_entry_rate_id_get(request: web.Request, time_entry_rate_id) -> web.Response:
    """View time entry rate

    

    :param time_entry_rate_id: 
    :type time_entry_rate_id: str
    :type time_entry_rate_id: str

    """
    return web.Response(status=200)


async def time_entry_rates_time_entry_rate_id_put(request: web.Request, time_entry_rate_id) -> web.Response:
    """Edit time entry rate

    

    :param time_entry_rate_id: 
    :type time_entry_rate_id: str
    :type time_entry_rate_id: str

    """
    return web.Response(status=200)
