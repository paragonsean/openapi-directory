from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.time_entry_types_get200_response import TimeEntryTypesGet200Response
from openapi_server.models.time_entry_types_post_request import TimeEntryTypesPostRequest
from openapi_server.models.time_entry_types_time_entry_type_id_get200_response import TimeEntryTypesTimeEntryTypeIdGet200Response
from openapi_server import util


async def bulk_activate_time_entry_types(request: web.Request, body) -> web.Response:
    """Bulk activate time entry types

    

    :param body: Time entry types ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def bulk_deactivate_time_entry_types(request: web.Request, body) -> web.Response:
    """Bulk deactivate time entry types

    

    :param body: Time entry types ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def bulk_delete_time_entry_types(request: web.Request, body) -> web.Response:
    """Bulk delete time entry types

    

    :param body: Time entry types ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def time_entry_types_get(request: web.Request, ) -> web.Response:
    """List time entries types

    


    """
    return web.Response(status=200)


async def time_entry_types_post(request: web.Request, body=None) -> web.Response:
    """Add new time entry type

    

    :param body: 
    :type body: dict | bytes

    """
    body = TimeEntryTypesPostRequest.from_dict(body)
    return web.Response(status=200)


async def time_entry_types_time_entry_type_id_delete(request: web.Request, time_entry_type_id) -> web.Response:
    """Delete time entry type

    

    :param time_entry_type_id: 
    :type time_entry_type_id: str
    :type time_entry_type_id: str

    """
    return web.Response(status=200)


async def time_entry_types_time_entry_type_id_get(request: web.Request, time_entry_type_id) -> web.Response:
    """View time entry type

    

    :param time_entry_type_id: 
    :type time_entry_type_id: str
    :type time_entry_type_id: str

    """
    return web.Response(status=200)


async def time_entry_types_time_entry_type_id_put(request: web.Request, time_entry_type_id) -> web.Response:
    """Edit time entry type

    

    :param time_entry_type_id: 
    :type time_entry_type_id: str
    :type time_entry_type_id: str

    """
    return web.Response(status=200)
