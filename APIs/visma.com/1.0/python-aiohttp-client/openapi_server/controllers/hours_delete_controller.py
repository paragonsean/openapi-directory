from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server import util


async def time_entries_delete_time_entry(request: web.Request, guid) -> web.Response:
    """Deletes a time entry.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the time entry.
    :type guid: str

    """
    return web.Response(status=200)


async def work_hours_delete_work_hour(request: web.Request, guid) -> web.Response:
    """Deletes a work hour.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the work hour.
    :type guid: str

    """
    return web.Response(status=200)
