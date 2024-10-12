from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_mobile_authorization_code_request import CreateMobileAuthorizationCodeRequest
from openapi_server.models.create_mobile_authorization_code_response import CreateMobileAuthorizationCodeResponse
from openapi_server import util


async def create_mobile_authorization_code(request: web.Request, body) -> web.Response:
    """CreateMobileAuthorizationCode

    Generates code to authorize a mobile application to connect to a Square card reader  Authorization codes are one-time-use and expire __60 minutes__ after being issued.  __Important:__ The &#x60;Authorization&#x60; header you provide to this endpoint must have the following format:  &#x60;&#x60;&#x60; Authorization: Bearer ACCESS_TOKEN &#x60;&#x60;&#x60;  Replace &#x60;ACCESS_TOKEN&#x60; with a [valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateMobileAuthorizationCodeRequest.from_dict(body)
    return web.Response(status=200)
