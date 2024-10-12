from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.event_response import EventResponse
from openapi_server.models.response import Response
from openapi_server.models.send_event_request import SendEventRequest
from openapi_server.models.send_user_custom_event_request import SendUserCustomEventRequest
from openapi_server.models.sync_request import SyncRequest
from openapi_server.models.sync_response import SyncResponse
from openapi_server import util


async def send_event(request: web.Request, type, id, body) -> web.Response:
    """Send event

    Sends event to the channel  Sends events: - any  Required permissions: - SendCustomEvent 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendEventRequest.from_dict(body)
    return web.Response(status=200)


async def send_user_custom_event(request: web.Request, user_id, body) -> web.Response:
    """Send user event

    Sends a custom event to a user  Sends events: - custom 

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendUserCustomEventRequest.from_dict(body)
    return web.Response(status=200)


async def sync_0(request: web.Request, body, with_inaccessible_cids=None, watch=None, client_id=None, connection_id=None) -> web.Response:
    """Sync

    Returns all events happened since client disconnect in specified channels  Required permissions: - ReadChannel 

    :param body: 
    :type body: dict | bytes
    :param with_inaccessible_cids: 
    :type with_inaccessible_cids: bool
    :param watch: 
    :type watch: bool
    :param client_id: 
    :type client_id: str
    :param connection_id: 
    :type connection_id: str

    """
    body = SyncRequest.from_dict(body)
    return web.Response(status=200)
