from typing import List, Dict
from aiohttp import web

from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.logs_request_body import LogsRequestBody
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server import util


async def get_logs(request: web.Request, body) -> web.Response:
    """Get logs

    

    :param body: 
    :type body: dict | bytes

    """
    body = LogsRequestBody.from_dict(body)
    return web.Response(status=200)
