from typing import List, Dict
from aiohttp import web

from openapi_server.models.log_entry import LogEntry
from openapi_server import util


async def log_delete(request: web.Request, ) -> web.Response:
    """log_delete

    delete all log messages


    """
    return web.Response(status=200)


async def log_get(request: web.Request, startindex=None, count=None, subject=None, type=None) -> web.Response:
    """log_get

    get a list of slicebox log messages

    :param startindex: start index of returned slice of log messages
    :type startindex: int
    :param count: size of returned slice of log messages
    :type count: int
    :param subject: log subject to filter results by
    :type subject: str
    :param type: log type (DEFAULT, INFO, WARN, ERROR) to filter results by
    :type type: str

    """
    return web.Response(status=200)


async def log_id_delete(request: web.Request, id) -> web.Response:
    """log_id_delete

    Delete the log entry with the supplied ID

    :param id: ID of log entry
    :type id: int

    """
    return web.Response(status=200)
