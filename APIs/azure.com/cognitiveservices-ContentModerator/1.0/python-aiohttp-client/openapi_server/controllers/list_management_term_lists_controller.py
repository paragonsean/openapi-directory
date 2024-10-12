from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.list_management_image_lists_create_request import ListManagementImageListsCreateRequest
from openapi_server.models.refresh_index import RefreshIndex
from openapi_server.models.term_list import TermList
from openapi_server import util


async def list_management_term_lists_create(request: web.Request, content_type, body) -> web.Response:
    """list_management_term_lists_create

    Creates a Term List

    :param content_type: The content type.
    :type content_type: str
    :param body: Schema of the body.
    :type body: dict | bytes

    """
    body = ListManagementImageListsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def list_management_term_lists_delete(request: web.Request, list_id) -> web.Response:
    """list_management_term_lists_delete

    Deletes term list with the list Id equal to list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str

    """
    return web.Response(status=200)


async def list_management_term_lists_get_all_term_lists(request: web.Request, ) -> web.Response:
    """list_management_term_lists_get_all_term_lists

    gets all the Term Lists


    """
    return web.Response(status=200)


async def list_management_term_lists_get_details(request: web.Request, list_id) -> web.Response:
    """list_management_term_lists_get_details

    Returns list Id details of the term list with list Id equal to list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str

    """
    return web.Response(status=200)


async def list_management_term_lists_refresh_index(request: web.Request, list_id, language) -> web.Response:
    """list_management_term_lists_refresh_index

    Refreshes the index of the list with list Id equal to list ID passed.

    :param list_id: List Id of the image list.
    :type list_id: str
    :param language: Language of the terms.
    :type language: str

    """
    return web.Response(status=200)


async def list_management_term_lists_update(request: web.Request, list_id, content_type, body) -> web.Response:
    """list_management_term_lists_update

    Updates an Term List.

    :param list_id: List Id of the image list.
    :type list_id: str
    :param content_type: The content type.
    :type content_type: str
    :param body: Schema of the body.
    :type body: dict | bytes

    """
    body = ListManagementImageListsCreateRequest.from_dict(body)
    return web.Response(status=200)
