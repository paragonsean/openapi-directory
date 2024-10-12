from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_sms_token_in import CreateSMSTokenIn
from openapi_server.models.create_sms_token_out import CreateSMSTokenOut
from openapi_server.models.verify_sms_token_out import VerifySMSTokenOut
from openapi_server import util


async def create_sms_token(request: web.Request, input) -> web.Response:
    """Create SMS token

    

    :param input: Input
    :type input: dict | bytes

    """
    input = CreateSMSTokenIn.from_dict(input)
    return web.Response(status=200)


async def verify_sms_token(request: web.Request, token) -> web.Response:
    """Verify SMS token

    

    :param token: Provided token.
    :type token: str

    """
    return web.Response(status=200)
