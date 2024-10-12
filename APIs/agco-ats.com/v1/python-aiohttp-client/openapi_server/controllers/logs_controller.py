from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_models_log import APIModelsLog
from openapi_server.models.api_paged_response_api_models_log import APIPagedResponseAPIModelsLog
from openapi_server import util


async def logs_get_log(request: web.Request, id) -> web.Response:
    """Get a log by ID

    No Documentation Found.

    :param id: The Log ID
    :type id: str

    """
    return web.Response(status=200)


async def logs_get_logs(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get the API System logs, most recent first.

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def logs_post_log(request: web.Request, message) -> web.Response:
    """Add a Log entry

    No Documentation Found.

    :param message: Message to enter into the log
    :type message: str

    """
    return web.Response(status=200)
