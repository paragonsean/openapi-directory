from typing import List, Dict
from aiohttp import web

from openapi_server.models.createnewappkey_request import CreatenewappkeyRequest
from openapi_server.models.createnewappkey_response import CreatenewappkeyResponse
from openapi_server.models.getappkeysfromaccount import Getappkeysfromaccount
from openapi_server.models.updateappkey_request import UpdateappkeyRequest
from openapi_server.models.vlm_error import VLMError
from openapi_server import util


async def createnewappkey(request: web.Request, body) -> web.Response:
    """Create new appkey

    Creates a new pair of &#x60;appKey&#x60; and &#x60;appToken&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = CreatenewappkeyRequest.from_dict(body)
    return web.Response(status=200)


async def getappkeysfromaccount(request: web.Request, content_type) -> web.Response:
    """Get appKeys from account

    Gets all application keys from an account.

    :param content_type: The media type of the body of the request. Default value for license manager protocol is application/json
    :type content_type: str

    """
    return web.Response(status=200)


async def updateappkey(request: web.Request, id, body) -> web.Response:
    """Update appkey

    Activates or deactivates an &#x60;appKey&#x60; by its ID.

    :param id: ID from the appKey which will be updated
    :type id: str
    :param body: Request body for updating AppKeys
    :type body: dict | bytes

    """
    body = UpdateappkeyRequest.from_dict(body)
    return web.Response(status=200)
