from typing import List, Dict
from aiohttp import web

from openapi_server.models.waterlinked_operation_response import WaterlinkedOperationResponse
from openapi_server.models.wl_warning import WlWarning
from openapi_server import util


async def warnings_get(request: web.Request, ) -> web.Response:
    """Get warnings

    [DEPRECATED] Get current list of messages


    """
    return web.Response(status=200)
