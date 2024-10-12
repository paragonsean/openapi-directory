from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.time_entries_get200_response import TimeEntriesGet200Response
from openapi_server.models.time_entries_post_request import TimeEntriesPostRequest
from openapi_server.models.time_entries_time_entry_id_get200_response import TimeEntriesTimeEntryIdGet200Response
from openapi_server import util


async def time_entries_get(request: web.Request, user_id=None, form_id=None, project_id=None, gt_from_time=None, lt_from_time=None, gt_to_time=None, lt_to_time=None, lt_sum=None, gt_sum=None) -> web.Response:
    """List time entries

    

    :param user_id: 
    :type user_id: str
    :param form_id: 
    :type form_id: str
    :param project_id: 
    :type project_id: str
    :param gt_from_time: 
    :type gt_from_time: str
    :param lt_from_time: 
    :type lt_from_time: str
    :param gt_to_time: 
    :type gt_to_time: str
    :param lt_to_time: 
    :type lt_to_time: str
    :param lt_sum: 
    :type lt_sum: str
    :param gt_sum: 
    :type gt_sum: str

    """
    return web.Response(status=200)


async def time_entries_post(request: web.Request, body=None) -> web.Response:
    """Add new time entry

    

    :param body: 
    :type body: dict | bytes

    """
    body = TimeEntriesPostRequest.from_dict(body)
    return web.Response(status=200)


async def time_entries_time_entry_id_delete(request: web.Request, time_entry_id) -> web.Response:
    """Delete time entry

    

    :param time_entry_id: 
    :type time_entry_id: str
    :type time_entry_id: str

    """
    return web.Response(status=200)


async def time_entries_time_entry_id_get(request: web.Request, time_entry_id) -> web.Response:
    """View time entry

    

    :param time_entry_id: 
    :type time_entry_id: str
    :type time_entry_id: str

    """
    return web.Response(status=200)


async def time_entries_time_entry_id_put(request: web.Request, time_entry_id) -> web.Response:
    """Edit time entry

    

    :param time_entry_id: 
    :type time_entry_id: str
    :type time_entry_id: str

    """
    return web.Response(status=200)
