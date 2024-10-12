from typing import List, Dict
from aiohttp import web

from openapi_server.models.register_account_request_body import RegisterAccountRequestBody
from openapi_server.models.request_code_request_body import RequestCodeRequestBody
from openapi_server.models.request_code_response import RequestCodeResponse
from openapi_server import util


async def register_account(request: web.Request, body) -> web.Response:
    """Register-Account

    

    :param body: 
    :type body: dict | bytes

    """
    body = RegisterAccountRequestBody.from_dict(body)
    return web.Response(status=200)


async def request_code(request: web.Request, body) -> web.Response:
    """Request-Code

    

    :param body: 
    :type body: dict | bytes

    """
    body = RequestCodeRequestBody.from_dict(body)
    return web.Response(status=200)
