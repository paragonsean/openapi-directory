from typing import List, Dict
from aiohttp import web

from openapi_server.models.append_chat_message_using_get200_response import AppendChatMessageUsingGET200Response
from openapi_server.models.append_chat_message_using_get400_response import AppendChatMessageUsingGET400Response
from openapi_server.models.append_chat_message_using_get401_response import AppendChatMessageUsingGET401Response
from openapi_server.models.append_chat_message_using_get500_response import AppendChatMessageUsingGET500Response
from openapi_server.models.create_group_using_get200_response import CreateGroupUsingGET200Response
from openapi_server.models.list_all_groups_using_get200_response import ListAllGroupsUsingGET200Response
from openapi_server.models.list_all_pads_using_get200_response import ListAllPadsUsingGET200Response
from openapi_server.models.list_sessions_of_author_using_get200_response import ListSessionsOfAuthorUsingGET200Response
from openapi_server import util


async def create_group_if_not_exists_for_using_get(request: web.Request, group_mapper=None) -> web.Response:
    """this functions helps you to map your application group ids to Etherpad group ids

    

    :param group_mapper: 
    :type group_mapper: str

    """
    return web.Response(status=200)


async def create_group_if_not_exists_for_using_post(request: web.Request, group_mapper=None) -> web.Response:
    """this functions helps you to map your application group ids to Etherpad group ids

    

    :param group_mapper: 
    :type group_mapper: str

    """
    return web.Response(status=200)


async def create_group_pad_using_get(request: web.Request, group_id=None, pad_name=None, text=None) -> web.Response:
    """creates a new pad in this group

    

    :param group_id: 
    :type group_id: str
    :param pad_name: 
    :type pad_name: str
    :param text: 
    :type text: str

    """
    return web.Response(status=200)


async def create_group_pad_using_post(request: web.Request, group_id=None, pad_name=None, text=None) -> web.Response:
    """creates a new pad in this group

    

    :param group_id: 
    :type group_id: str
    :param pad_name: 
    :type pad_name: str
    :param text: 
    :type text: str

    """
    return web.Response(status=200)


async def create_group_using_get(request: web.Request, ) -> web.Response:
    """creates a new group

    


    """
    return web.Response(status=200)


async def create_group_using_post(request: web.Request, ) -> web.Response:
    """creates a new group

    


    """
    return web.Response(status=200)


async def delete_group_using_get(request: web.Request, group_id=None) -> web.Response:
    """deletes a group

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def delete_group_using_post(request: web.Request, group_id=None) -> web.Response:
    """deletes a group

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def list_all_groups_using_get(request: web.Request, ) -> web.Response:
    """

    


    """
    return web.Response(status=200)


async def list_all_groups_using_post(request: web.Request, ) -> web.Response:
    """

    


    """
    return web.Response(status=200)


async def list_pads_using_get(request: web.Request, group_id=None) -> web.Response:
    """returns all pads of this group

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def list_pads_using_post(request: web.Request, group_id=None) -> web.Response:
    """returns all pads of this group

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def list_sessions_of_group_using_get(request: web.Request, group_id=None) -> web.Response:
    """

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def list_sessions_of_group_using_post(request: web.Request, group_id=None) -> web.Response:
    """

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)
