from typing import List, Dict
from aiohttp import web

from openapi_server.models.play_media_request import PlayMediaRequest
from openapi_server.models.queue import Queue
from openapi_server.models.update_activity_request import UpdateActivityRequest
from openapi_server.models.update_activity_response import UpdateActivityResponse
from openapi_server import util


async def play_media_on_queue(request: web.Request, x_applecloudextension_session_id, user_agent, accept_language, x_applecloudextension_retry_count=None, body=None) -> web.Response:
    """playMedia

    

    :param x_applecloudextension_session_id: 
    :type x_applecloudextension_session_id: str
    :param user_agent: 
    :type user_agent: str
    :param accept_language: 
    :type accept_language: str
    :param x_applecloudextension_retry_count: 
    :type x_applecloudextension_retry_count: 
    :param body: 
    :type body: dict | bytes

    """
    body = PlayMediaRequest.from_dict(body)
    return web.Response(status=200)


async def update_activity_on_queue(request: web.Request, x_applecloudextension_session_id, user_agent, accept_language, x_applecloudextension_retry_count=None, body=None) -> web.Response:
    """updateActivity

    

    :param x_applecloudextension_session_id: 
    :type x_applecloudextension_session_id: str
    :param user_agent: 
    :type user_agent: str
    :param accept_language: 
    :type accept_language: str
    :param x_applecloudextension_retry_count: 
    :type x_applecloudextension_retry_count: 
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateActivityRequest.from_dict(body)
    return web.Response(status=200)
