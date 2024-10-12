from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def media_tabular_extractsheet(request: web.Request, output, entryid, arg1=None) -> web.Response:
    """API for Extract sheets

    API to call: Extract sheets

    :param output: Output type  -don&#39;t change
    :type output: str
    :param entryid: Entry ID
    :type entryid: str
    :param arg1: Sheets
    :type arg1: str

    """
    return web.Response(status=200)
