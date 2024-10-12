from typing import List, Dict
from aiohttp import web

from openapi_server.models.validate_for_voice200_response import ValidateForVoice200Response
from openapi_server import util


async def validate_for_voice(request: web.Request, number, param_callback=None) -> web.Response:
    """validate_for_voice

    

    :param number: Determines the recipient. Can only be a number, not a contact from your address book.
    :type number: str
    :param param_callback: The callback URL which gets queried right after validation.
    :type param_callback: str

    """
    return web.Response(status=200)
