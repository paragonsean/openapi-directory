from typing import List, Dict
from aiohttp import web

from openapi_server.models.append_chat_message_using_get200_response import AppendChatMessageUsingGET200Response
from openapi_server.models.append_chat_message_using_get400_response import AppendChatMessageUsingGET400Response
from openapi_server.models.append_chat_message_using_get401_response import AppendChatMessageUsingGET401Response
from openapi_server.models.append_chat_message_using_get500_response import AppendChatMessageUsingGET500Response
from openapi_server import util


async def append_text_using_get(request: web.Request, pad_id=None, text=None) -> web.Response:
    """append_text_using_get

    

    :param pad_id: 
    :type pad_id: str
    :param text: 
    :type text: str

    """
    return web.Response(status=200)


async def append_text_using_post(request: web.Request, pad_id=None, text=None) -> web.Response:
    """append_text_using_post

    

    :param pad_id: 
    :type pad_id: str
    :param text: 
    :type text: str

    """
    return web.Response(status=200)


async def copy_pad_using_get(request: web.Request, source_id=None, destination_id=None, force=None) -> web.Response:
    """copy_pad_using_get

    

    :param source_id: 
    :type source_id: str
    :param destination_id: 
    :type destination_id: str
    :param force: 
    :type force: str

    """
    return web.Response(status=200)


async def copy_pad_using_post(request: web.Request, source_id=None, destination_id=None, force=None) -> web.Response:
    """copy_pad_using_post

    

    :param source_id: 
    :type source_id: str
    :param destination_id: 
    :type destination_id: str
    :param force: 
    :type force: str

    """
    return web.Response(status=200)


async def copy_pad_without_history_using_get(request: web.Request, source_id=None, destination_id=None, force=None) -> web.Response:
    """copy_pad_without_history_using_get

    

    :param source_id: 
    :type source_id: str
    :param destination_id: 
    :type destination_id: str
    :param force: 
    :type force: str

    """
    return web.Response(status=200)


async def copy_pad_without_history_using_post(request: web.Request, source_id=None, destination_id=None, force=None) -> web.Response:
    """copy_pad_without_history_using_post

    

    :param source_id: 
    :type source_id: str
    :param destination_id: 
    :type destination_id: str
    :param force: 
    :type force: str

    """
    return web.Response(status=200)


async def get_attribute_pool_using_get(request: web.Request, pad_id=None) -> web.Response:
    """get_attribute_pool_using_get

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_attribute_pool_using_post(request: web.Request, pad_id=None) -> web.Response:
    """get_attribute_pool_using_post

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_pad_id_using_get(request: web.Request, ro_id=None) -> web.Response:
    """get_pad_id_using_get

    

    :param ro_id: 
    :type ro_id: str

    """
    return web.Response(status=200)


async def get_pad_id_using_post(request: web.Request, ro_id=None) -> web.Response:
    """get_pad_id_using_post

    

    :param ro_id: 
    :type ro_id: str

    """
    return web.Response(status=200)


async def get_revision_changeset_using_get(request: web.Request, pad_id=None, rev=None) -> web.Response:
    """get_revision_changeset_using_get

    

    :param pad_id: 
    :type pad_id: str
    :param rev: 
    :type rev: str

    """
    return web.Response(status=200)


async def get_revision_changeset_using_post(request: web.Request, pad_id=None, rev=None) -> web.Response:
    """get_revision_changeset_using_post

    

    :param pad_id: 
    :type pad_id: str
    :param rev: 
    :type rev: str

    """
    return web.Response(status=200)


async def get_saved_revisions_count_using_get(request: web.Request, pad_id=None) -> web.Response:
    """get_saved_revisions_count_using_get

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_saved_revisions_count_using_post(request: web.Request, pad_id=None) -> web.Response:
    """get_saved_revisions_count_using_post

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_stats_using_get(request: web.Request, ) -> web.Response:
    """get_stats_using_get

    


    """
    return web.Response(status=200)


async def get_stats_using_post(request: web.Request, ) -> web.Response:
    """get_stats_using_post

    


    """
    return web.Response(status=200)


async def list_saved_revisions_using_get(request: web.Request, pad_id=None) -> web.Response:
    """list_saved_revisions_using_get

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def list_saved_revisions_using_post(request: web.Request, pad_id=None) -> web.Response:
    """list_saved_revisions_using_post

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def move_pad_using_get(request: web.Request, source_id=None, destination_id=None, force=None) -> web.Response:
    """move_pad_using_get

    

    :param source_id: 
    :type source_id: str
    :param destination_id: 
    :type destination_id: str
    :param force: 
    :type force: str

    """
    return web.Response(status=200)


async def move_pad_using_post(request: web.Request, source_id=None, destination_id=None, force=None) -> web.Response:
    """move_pad_using_post

    

    :param source_id: 
    :type source_id: str
    :param destination_id: 
    :type destination_id: str
    :param force: 
    :type force: str

    """
    return web.Response(status=200)


async def restore_revision_using_get(request: web.Request, pad_id=None, rev=None) -> web.Response:
    """restore_revision_using_get

    

    :param pad_id: 
    :type pad_id: str
    :param rev: 
    :type rev: str

    """
    return web.Response(status=200)


async def restore_revision_using_post(request: web.Request, pad_id=None, rev=None) -> web.Response:
    """restore_revision_using_post

    

    :param pad_id: 
    :type pad_id: str
    :param rev: 
    :type rev: str

    """
    return web.Response(status=200)


async def save_revision_using_get(request: web.Request, pad_id=None, rev=None) -> web.Response:
    """save_revision_using_get

    

    :param pad_id: 
    :type pad_id: str
    :param rev: 
    :type rev: str

    """
    return web.Response(status=200)


async def save_revision_using_post(request: web.Request, pad_id=None, rev=None) -> web.Response:
    """save_revision_using_post

    

    :param pad_id: 
    :type pad_id: str
    :param rev: 
    :type rev: str

    """
    return web.Response(status=200)
