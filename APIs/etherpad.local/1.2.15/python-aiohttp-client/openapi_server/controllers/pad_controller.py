from typing import List, Dict
from aiohttp import web

from openapi_server.models.append_chat_message_using_get200_response import AppendChatMessageUsingGET200Response
from openapi_server.models.append_chat_message_using_get400_response import AppendChatMessageUsingGET400Response
from openapi_server.models.append_chat_message_using_get401_response import AppendChatMessageUsingGET401Response
from openapi_server.models.append_chat_message_using_get500_response import AppendChatMessageUsingGET500Response
from openapi_server.models.create_diff_html_using_get200_response import CreateDiffHTMLUsingGET200Response
from openapi_server.models.get_chat_head_using_get200_response import GetChatHeadUsingGET200Response
from openapi_server.models.get_chat_history_using_get200_response import GetChatHistoryUsingGET200Response
from openapi_server.models.get_html_using_get200_response import GetHTMLUsingGET200Response
from openapi_server.models.get_last_edited_using_get200_response import GetLastEditedUsingGET200Response
from openapi_server.models.get_public_status_using_get200_response import GetPublicStatusUsingGET200Response
from openapi_server.models.get_read_only_id_using_get200_response import GetReadOnlyIDUsingGET200Response
from openapi_server.models.get_revisions_count_using_get200_response import GetRevisionsCountUsingGET200Response
from openapi_server.models.get_text_using_get200_response import GetTextUsingGET200Response
from openapi_server.models.list_all_pads_using_get200_response import ListAllPadsUsingGET200Response
from openapi_server.models.list_authors_of_pad_using_get200_response import ListAuthorsOfPadUsingGET200Response
from openapi_server.models.pad_users_count_using_get200_response import PadUsersCountUsingGET200Response
from openapi_server.models.pad_users_using_get200_response import PadUsersUsingGET200Response
from openapi_server import util


async def append_chat_message_using_get(request: web.Request, pad_id=None, text=None, author_id=None, time=None) -> web.Response:
    """appends a chat message

    

    :param pad_id: 
    :type pad_id: str
    :param text: 
    :type text: str
    :param author_id: 
    :type author_id: str
    :param time: 
    :type time: str

    """
    return web.Response(status=200)


async def append_chat_message_using_post(request: web.Request, pad_id=None, text=None, author_id=None, time=None) -> web.Response:
    """appends a chat message

    

    :param pad_id: 
    :type pad_id: str
    :param text: 
    :type text: str
    :param author_id: 
    :type author_id: str
    :param time: 
    :type time: str

    """
    return web.Response(status=200)


async def check_token_using_get(request: web.Request, ) -> web.Response:
    """returns ok when the current api token is valid

    


    """
    return web.Response(status=200)


async def check_token_using_post(request: web.Request, ) -> web.Response:
    """returns ok when the current api token is valid

    


    """
    return web.Response(status=200)


async def create_diff_html_using_get(request: web.Request, pad_id=None, start_rev=None, end_rev=None) -> web.Response:
    """

    

    :param pad_id: 
    :type pad_id: str
    :param start_rev: 
    :type start_rev: str
    :param end_rev: 
    :type end_rev: str

    """
    return web.Response(status=200)


async def create_diff_html_using_post(request: web.Request, pad_id=None, start_rev=None, end_rev=None) -> web.Response:
    """

    

    :param pad_id: 
    :type pad_id: str
    :param start_rev: 
    :type start_rev: str
    :param end_rev: 
    :type end_rev: str

    """
    return web.Response(status=200)


async def create_pad_using_get(request: web.Request, pad_id=None, text=None) -> web.Response:
    """create_pad_using_get

    creates a new (non-group) pad. Note that if you need to create a group Pad, you should call createGroupPad

    :param pad_id: 
    :type pad_id: str
    :param text: 
    :type text: str

    """
    return web.Response(status=200)


async def create_pad_using_post(request: web.Request, pad_id=None, text=None) -> web.Response:
    """create_pad_using_post

    creates a new (non-group) pad. Note that if you need to create a group Pad, you should call createGroupPad

    :param pad_id: 
    :type pad_id: str
    :param text: 
    :type text: str

    """
    return web.Response(status=200)


async def delete_pad_using_get(request: web.Request, pad_id=None) -> web.Response:
    """deletes a pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def delete_pad_using_post(request: web.Request, pad_id=None) -> web.Response:
    """deletes a pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_chat_head_using_get(request: web.Request, pad_id=None) -> web.Response:
    """returns the chatHead (chat-message) of the pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_chat_head_using_post(request: web.Request, pad_id=None) -> web.Response:
    """returns the chatHead (chat-message) of the pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_chat_history_using_get(request: web.Request, pad_id=None, start=None, end=None) -> web.Response:
    """returns the chat history

    

    :param pad_id: 
    :type pad_id: str
    :param start: 
    :type start: str
    :param end: 
    :type end: str

    """
    return web.Response(status=200)


async def get_chat_history_using_post(request: web.Request, pad_id=None, start=None, end=None) -> web.Response:
    """returns the chat history

    

    :param pad_id: 
    :type pad_id: str
    :param start: 
    :type start: str
    :param end: 
    :type end: str

    """
    return web.Response(status=200)


async def get_html_using_get(request: web.Request, pad_id=None, rev=None) -> web.Response:
    """returns the text of a pad formatted as HTML

    

    :param pad_id: 
    :type pad_id: str
    :param rev: 
    :type rev: str

    """
    return web.Response(status=200)


async def get_html_using_post(request: web.Request, pad_id=None, rev=None) -> web.Response:
    """returns the text of a pad formatted as HTML

    

    :param pad_id: 
    :type pad_id: str
    :param rev: 
    :type rev: str

    """
    return web.Response(status=200)


async def get_last_edited_using_get(request: web.Request, pad_id=None) -> web.Response:
    """returns the timestamp of the last revision of the pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_last_edited_using_post(request: web.Request, pad_id=None) -> web.Response:
    """returns the timestamp of the last revision of the pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_public_status_using_get(request: web.Request, pad_id=None) -> web.Response:
    """return true of false

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_public_status_using_post(request: web.Request, pad_id=None) -> web.Response:
    """return true of false

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_read_only_id_using_get(request: web.Request, pad_id=None) -> web.Response:
    """returns the read only link of a pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_read_only_id_using_post(request: web.Request, pad_id=None) -> web.Response:
    """returns the read only link of a pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_revisions_count_using_get(request: web.Request, pad_id=None) -> web.Response:
    """returns the number of revisions of this pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_revisions_count_using_post(request: web.Request, pad_id=None) -> web.Response:
    """returns the number of revisions of this pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def get_text_using_get(request: web.Request, pad_id=None, rev=None) -> web.Response:
    """returns the text of a pad

    

    :param pad_id: 
    :type pad_id: str
    :param rev: 
    :type rev: str

    """
    return web.Response(status=200)


async def get_text_using_post(request: web.Request, pad_id=None, rev=None) -> web.Response:
    """returns the text of a pad

    

    :param pad_id: 
    :type pad_id: str
    :param rev: 
    :type rev: str

    """
    return web.Response(status=200)


async def list_all_pads_using_get(request: web.Request, ) -> web.Response:
    """list all the pads

    


    """
    return web.Response(status=200)


async def list_all_pads_using_post(request: web.Request, ) -> web.Response:
    """list all the pads

    


    """
    return web.Response(status=200)


async def list_authors_of_pad_using_get(request: web.Request, pad_id=None) -> web.Response:
    """returns an array of authors who contributed to this pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def list_authors_of_pad_using_post(request: web.Request, pad_id=None) -> web.Response:
    """returns an array of authors who contributed to this pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def pad_users_count_using_get(request: web.Request, pad_id=None) -> web.Response:
    """returns the number of user that are currently editing this pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def pad_users_count_using_post(request: web.Request, pad_id=None) -> web.Response:
    """returns the number of user that are currently editing this pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def pad_users_using_get(request: web.Request, pad_id=None) -> web.Response:
    """returns the list of users that are currently editing this pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def pad_users_using_post(request: web.Request, pad_id=None) -> web.Response:
    """returns the list of users that are currently editing this pad

    

    :param pad_id: 
    :type pad_id: str

    """
    return web.Response(status=200)


async def send_clients_message_using_get(request: web.Request, pad_id=None, msg=None) -> web.Response:
    """sends a custom message of type msg to the pad

    

    :param pad_id: 
    :type pad_id: str
    :param msg: 
    :type msg: str

    """
    return web.Response(status=200)


async def send_clients_message_using_post(request: web.Request, pad_id=None, msg=None) -> web.Response:
    """sends a custom message of type msg to the pad

    

    :param pad_id: 
    :type pad_id: str
    :param msg: 
    :type msg: str

    """
    return web.Response(status=200)


async def set_html_using_get(request: web.Request, pad_id=None, html=None) -> web.Response:
    """sets the text of a pad with HTML

    

    :param pad_id: 
    :type pad_id: str
    :param html: 
    :type html: str

    """
    return web.Response(status=200)


async def set_html_using_post(request: web.Request, pad_id=None, html=None) -> web.Response:
    """sets the text of a pad with HTML

    

    :param pad_id: 
    :type pad_id: str
    :param html: 
    :type html: str

    """
    return web.Response(status=200)


async def set_public_status_using_get(request: web.Request, pad_id=None, public_status=None) -> web.Response:
    """sets a boolean for the public status of a pad

    

    :param pad_id: 
    :type pad_id: str
    :param public_status: 
    :type public_status: str

    """
    return web.Response(status=200)


async def set_public_status_using_post(request: web.Request, pad_id=None, public_status=None) -> web.Response:
    """sets a boolean for the public status of a pad

    

    :param pad_id: 
    :type pad_id: str
    :param public_status: 
    :type public_status: str

    """
    return web.Response(status=200)


async def set_text_using_get(request: web.Request, pad_id=None, text=None) -> web.Response:
    """sets the text of a pad

    

    :param pad_id: 
    :type pad_id: str
    :param text: 
    :type text: str

    """
    return web.Response(status=200)


async def set_text_using_post(request: web.Request, pad_id=None, text=None) -> web.Response:
    """sets the text of a pad

    

    :param pad_id: 
    :type pad_id: str
    :param text: 
    :type text: str

    """
    return web.Response(status=200)
