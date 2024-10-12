from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_preview_create_request import AppPreviewCreateRequest
from openapi_server.models.app_preview_response import AppPreviewResponse
from openapi_server.models.app_preview_update_request import AppPreviewUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_previews_create_instance(request: web.Request, body) -> web.Response:
    """app_previews_create_instance

    

    :param body: AppPreview representation
    :type body: dict | bytes

    """
    body = AppPreviewCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_previews_delete_instance(request: web.Request, id) -> web.Response:
    """app_previews_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_previews_get_instance(request: web.Request, id, fields_app_previews=None, include=None) -> web.Response:
    """app_previews_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_previews: the fields to include for returned resources of type appPreviews
    :type fields_app_previews: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_previews_update_instance(request: web.Request, id, body) -> web.Response:
    """app_previews_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AppPreview representation
    :type body: dict | bytes

    """
    body = AppPreviewUpdateRequest.from_dict(body)
    return web.Response(status=200)
