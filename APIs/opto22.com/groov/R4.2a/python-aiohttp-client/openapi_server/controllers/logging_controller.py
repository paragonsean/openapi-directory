from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def download_log_json(request: web.Request, minimum_log_level=None, last_timestamp=None, filter=None) -> web.Response:
    """download_log_json

    Downloads the complete groov View log in JSON format. Added in groov View R4.2a.

    :param minimum_log_level: How verbose the log should be.
    :type minimum_log_level: str
    :param last_timestamp: The earliest time to include in the log. Value is milliseconds since January 1, 1970 UTC.
    :type last_timestamp: 
    :param filter: Optional string to search for in the log.
    :type filter: str

    """
    return web.Response(status=200)


async def download_log_text(request: web.Request, minimum_log_level=None, last_timestamp=None, filter=None) -> web.Response:
    """download_log_text

    Downloads the complete groov View log. Added in groov View R4.2a.

    :param minimum_log_level: How verbose the log should be.
    :type minimum_log_level: str
    :param last_timestamp: The earliest time to include in the log. Value is milliseconds since January 1, 1970 UTC.
    :type last_timestamp: 
    :param filter: Optional string to search for in the log.
    :type filter: str

    """
    return web.Response(status=200)
