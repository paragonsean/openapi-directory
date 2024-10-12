from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.check_push_request import CheckPushRequest
from openapi_server.models.check_push_response import CheckPushResponse
from openapi_server.models.check_sqs_request import CheckSQSRequest
from openapi_server.models.check_sqs_response import CheckSQSResponse
from openapi_server import util


async def check_push_0(request: web.Request, body) -> web.Response:
    """Check push

    Sends a test message via push, this is a test endpoint to verify your push settings 

    :param body: 
    :type body: dict | bytes

    """
    body = CheckPushRequest.from_dict(body)
    return web.Response(status=200)


async def check_sqs_0(request: web.Request, body) -> web.Response:
    """Check SQS

    Validates Amazon SQS credentials 

    :param body: 
    :type body: dict | bytes

    """
    body = CheckSQSRequest.from_dict(body)
    return web.Response(status=200)
