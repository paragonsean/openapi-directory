from typing import List, Dict
from aiohttp import web

from openapi_server.models.append_chat_message_using_get400_response import AppendChatMessageUsingGET400Response
from openapi_server.models.append_chat_message_using_get401_response import AppendChatMessageUsingGET401Response
from openapi_server.models.append_chat_message_using_get500_response import AppendChatMessageUsingGET500Response
from openapi_server.models.create_author_using_get200_response import CreateAuthorUsingGET200Response
from openapi_server.models.get_author_name_using_get200_response import GetAuthorNameUsingGET200Response
from openapi_server.models.list_all_pads_using_get200_response import ListAllPadsUsingGET200Response
from openapi_server.models.list_sessions_of_author_using_get200_response import ListSessionsOfAuthorUsingGET200Response
from openapi_server import util


async def create_author_if_not_exists_for_using_get(request: web.Request, author_mapper=None, name=None) -> web.Response:
    """this functions helps you to map your application author ids to Etherpad author ids

    

    :param author_mapper: 
    :type author_mapper: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def create_author_if_not_exists_for_using_post(request: web.Request, author_mapper=None, name=None) -> web.Response:
    """this functions helps you to map your application author ids to Etherpad author ids

    

    :param author_mapper: 
    :type author_mapper: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def create_author_using_get(request: web.Request, name=None) -> web.Response:
    """creates a new author

    

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def create_author_using_post(request: web.Request, name=None) -> web.Response:
    """creates a new author

    

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_author_name_using_get(request: web.Request, author_id=None) -> web.Response:
    """Returns the Author Name of the author

    

    :param author_id: 
    :type author_id: str

    """
    return web.Response(status=200)


async def get_author_name_using_post(request: web.Request, author_id=None) -> web.Response:
    """Returns the Author Name of the author

    

    :param author_id: 
    :type author_id: str

    """
    return web.Response(status=200)


async def list_pads_of_author_using_get(request: web.Request, author_id=None) -> web.Response:
    """returns an array of all pads this author contributed to

    

    :param author_id: 
    :type author_id: str

    """
    return web.Response(status=200)


async def list_pads_of_author_using_post(request: web.Request, author_id=None) -> web.Response:
    """returns an array of all pads this author contributed to

    

    :param author_id: 
    :type author_id: str

    """
    return web.Response(status=200)


async def list_sessions_of_author_using_get(request: web.Request, author_id=None) -> web.Response:
    """returns all sessions of an author

    

    :param author_id: 
    :type author_id: str

    """
    return web.Response(status=200)


async def list_sessions_of_author_using_post(request: web.Request, author_id=None) -> web.Response:
    """returns all sessions of an author

    

    :param author_id: 
    :type author_id: str

    """
    return web.Response(status=200)
