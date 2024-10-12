from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.time_entry_model import TimeEntryModel
from openapi_server.models.work_hour_input_model import WorkHourInputModel
from openapi_server.models.work_hour_output_model import WorkHourOutputModel
from openapi_server import util


async def time_entries_patch_time_entry(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a time entry or a part of it.

    

    :param guid: ID of the time entry.
    :type guid: str
    :param body: JSON Patch document of TimeEntryModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def time_entries_post_time_entry(request: web.Request, body=None) -> web.Response:
    """Insert a time entry.

    

    :param body: TimeEntryModel.
    :type body: dict | bytes

    """
    body = TimeEntryModel.from_dict(body)
    return web.Response(status=200)


async def work_hours_patch_work_hour(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a work hour or a part of it

    

    :param guid: ID of the work hour. Can also be comma separate list of IDs to patch multiple work hours with one call. When multiple IDs are given, returns model which has list of succeeded work hours and list of errors.
    :type guid: str
    :param body: JSON Patch document of WorkHourInputModel
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def work_hours_post_work_hour(request: web.Request, body=None) -> web.Response:
    """Insert a work hour

    

    :param body: WorkHourInputModel
    :type body: dict | bytes

    """
    body = WorkHourInputModel.from_dict(body)
    return web.Response(status=200)
