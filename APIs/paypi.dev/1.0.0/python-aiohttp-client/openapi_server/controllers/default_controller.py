from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_code_post200_response import CheckCodePost200Response
from openapi_server.models.check_code_post401_response import CheckCodePost401Response
from openapi_server.models.check_code_post403_response import CheckCodePost403Response
from openapi_server.models.check_code_post_request import CheckCodePostRequest
from openapi_server.models.send_code_post200_response import SendCodePost200Response
from openapi_server.models.send_code_post400_response import SendCodePost400Response
from openapi_server.models.send_code_post_request import SendCodePostRequest
from openapi_server import util


async def check_code_post(request: web.Request, body) -> web.Response:
    """Check verification code

    Checks the user&#39;s emailed code is valid.  If this returns success&#x3D;true, you can safely assume the user you are interacting with is the owner of that email address. 

    :param body: 
    :type body: dict | bytes

    """
    body = CheckCodePostRequest.from_dict(body)
    return web.Response(status=200)


async def send_code_post(request: web.Request, body) -> web.Response:
    """Send verification code

    This request send&#39;s a code to the given email address, which should be returned to check it is correct.

    :param body: 
    :type body: dict | bytes

    """
    body = SendCodePostRequest.from_dict(body)
    return web.Response(status=200)
