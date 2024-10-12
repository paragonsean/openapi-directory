from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_call_request import CreateCallRequest
from openapi_server.models.create_call_response import CreateCallResponse
from openapi_server.models.get_call_token_request import GetCallTokenRequest
from openapi_server.models.get_call_token_response import GetCallTokenResponse
from openapi_server.models.message_response import MessageResponse
from openapi_server import util


async def commit_message(request: web.Request, id) -> web.Response:
    """Commit message

    Commits a pending message, which will make it visible in the channel  Sends events: - message.new - message.updated 

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def create_call(request: web.Request, type, id, body) -> web.Response:
    """Create a call

    Creates a call  Required permissions: - CreateCall - ReadChannel 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCallRequest.from_dict(body)
    return web.Response(status=200)


async def get_call_token1(request: web.Request, body) -> web.Response:
    """Get Call Token ()

    Retrieves the token to join a call  Required permissions: - JoinCall - ReadChannel 

    :param body: 
    :type body: dict | bytes

    """
    body = GetCallTokenRequest.from_dict(body)
    return web.Response(status=200)


async def get_call_token_call_id0(request: web.Request, call_id, body) -> web.Response:
    """Get Call Token (call_id)

    Retrieves the token to join a call  Required permissions: - JoinCall - ReadChannel 

    :param call_id: 
    :type call_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetCallTokenRequest.from_dict(body)
    return web.Response(status=200)
