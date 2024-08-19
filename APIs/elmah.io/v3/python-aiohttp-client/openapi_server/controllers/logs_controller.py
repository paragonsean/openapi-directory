from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_log import CreateLog
from openapi_server.models.create_log_result import CreateLogResult
from openapi_server.models.log import Log
from openapi_server import util


async def logs_create(request: web.Request, body=None) -> web.Response:
    """Create a new log.

    Required permission: &#x60;logs_write&#x60;

    :param body: The log object to create.
    :type body: dict | bytes

    """
    body = CreateLog.from_dict(body)
    return web.Response(status=200)


async def logs_diagnose(request: web.Request, id) -> web.Response:
    """Help diagnose logging problems.

    Required permission: &#x60;messages_write&#x60;

    :param id: The ID of the log to diagnose.
    :type id: str

    """
    return web.Response(status=200)


async def logs_disable(request: web.Request, id) -> web.Response:
    """Disable a log by its ID.

    Required permission: &#x60;logs_write&#x60;

    :param id: The ID of the log to disable.
    :type id: str

    """
    return web.Response(status=200)


async def logs_enable(request: web.Request, id) -> web.Response:
    """Enable a log by its ID.

    Required permission: &#x60;logs_write&#x60;

    :param id: The ID of the log to enable.
    :type id: str

    """
    return web.Response(status=200)


async def logs_get(request: web.Request, id) -> web.Response:
    """Fetch a log by its ID.

    Required permission: &#x60;logs_read&#x60;

    :param id: The ID of the log to fetch.
    :type id: str

    """
    return web.Response(status=200)


async def logs_get_all(request: web.Request, ) -> web.Response:
    """Fetch a list of logs.

    Required permission: &#x60;logs_read&#x60;


    """
    return web.Response(status=200)
