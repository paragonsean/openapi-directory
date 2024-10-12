from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.image_list import ImageList
from openapi_server.models.list_management_image_lists_create_request import ListManagementImageListsCreateRequest
from openapi_server.models.refresh_index import RefreshIndex
from openapi_server import util


async def list_management_image_lists_create(request: web.Request, content_type, body) -> web.Response:
    """list_management_image_lists_create

    Creates an image list.

    :param content_type: The content type.
    :type content_type: str
    :param body: Schema of the body.
    :type body: dict | bytes

    """
    body = ListManagementImageListsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def list_management_image_lists_delete(request: web.Request, list_id) -> web.Response:
    """list_management_image_lists_delete

    Deletes image list with the list Id equal to list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str

    """
    return web.Response(status=200)


async def list_management_image_lists_get_all_image_lists(request: web.Request, ) -> web.Response:
    """list_management_image_lists_get_all_image_lists

    Gets all the Image Lists.


    """
    return web.Response(status=200)


async def list_management_image_lists_get_details(request: web.Request, list_id) -> web.Response:
    """list_management_image_lists_get_details

    Returns the details of the image list with list Id equal to list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str

    """
    return web.Response(status=200)


async def list_management_image_lists_refresh_index(request: web.Request, list_id) -> web.Response:
    """list_management_image_lists_refresh_index

    Refreshes the index of the list with list Id equal to list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str

    """
    return web.Response(status=200)


async def list_management_image_lists_update(request: web.Request, list_id, content_type, body) -> web.Response:
    """list_management_image_lists_update

    Updates an image list with list Id equal to list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str
    :param content_type: The content type.
    :type content_type: str
    :param body: Schema of the body.
    :type body: dict | bytes

    """
    body = ListManagementImageListsCreateRequest.from_dict(body)
    return web.Response(status=200)
