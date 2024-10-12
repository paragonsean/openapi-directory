from typing import List, Dict
from aiohttp import web

from openapi_server.models.append_chat_message_using_get200_response import AppendChatMessageUsingGET200Response
from openapi_server.models.append_chat_message_using_get400_response import AppendChatMessageUsingGET400Response
from openapi_server.models.append_chat_message_using_get401_response import AppendChatMessageUsingGET401Response
from openapi_server.models.append_chat_message_using_get500_response import AppendChatMessageUsingGET500Response
from openapi_server.models.create_session_using_get200_response import CreateSessionUsingGET200Response
from openapi_server.models.get_session_info_using_get200_response import GetSessionInfoUsingGET200Response
from openapi_server import util


async def create_session_using_get(request: web.Request, group_id=None, author_id=None, valid_until=None) -> web.Response:
    """creates a new session. validUntil is an unix timestamp in seconds

    

    :param group_id: 
    :type group_id: str
    :param author_id: 
    :type author_id: str
    :param valid_until: 
    :type valid_until: str

    """
    return web.Response(status=200)


async def create_session_using_post(request: web.Request, group_id=None, author_id=None, valid_until=None) -> web.Response:
    """creates a new session. validUntil is an unix timestamp in seconds

    

    :param group_id: 
    :type group_id: str
    :param author_id: 
    :type author_id: str
    :param valid_until: 
    :type valid_until: str

    """
    return web.Response(status=200)


async def delete_session_using_get(request: web.Request, session_id=None) -> web.Response:
    """deletes a session

    

    :param session_id: 
    :type session_id: str

    """
    return web.Response(status=200)


async def delete_session_using_post(request: web.Request, session_id=None) -> web.Response:
    """deletes a session

    

    :param session_id: 
    :type session_id: str

    """
    return web.Response(status=200)


async def get_session_info_using_get(request: web.Request, session_id=None) -> web.Response:
    """returns informations about a session

    

    :param session_id: 
    :type session_id: str

    """
    return web.Response(status=200)


async def get_session_info_using_post(request: web.Request, session_id=None) -> web.Response:
    """returns informations about a session

    

    :param session_id: 
    :type session_id: str

    """
    return web.Response(status=200)
