from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_preview_set_app_previews_linkages_request import AppPreviewSetAppPreviewsLinkagesRequest
from openapi_server.models.app_preview_set_app_previews_linkages_response import AppPreviewSetAppPreviewsLinkagesResponse
from openapi_server.models.app_preview_set_create_request import AppPreviewSetCreateRequest
from openapi_server.models.app_preview_set_response import AppPreviewSetResponse
from openapi_server.models.app_previews_response import AppPreviewsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_preview_sets_app_previews_get_to_many_related(request: web.Request, id, fields_app_previews=None, fields_app_preview_sets=None, limit=None, include=None) -> web.Response:
    """app_preview_sets_app_previews_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_previews: the fields to include for returned resources of type appPreviews
    :type fields_app_previews: List[str]
    :param fields_app_preview_sets: the fields to include for returned resources of type appPreviewSets
    :type fields_app_preview_sets: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_preview_sets_app_previews_get_to_many_relationship(request: web.Request, id, limit=None) -> web.Response:
    """app_preview_sets_app_previews_get_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def app_preview_sets_app_previews_replace_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """app_preview_sets_app_previews_replace_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = AppPreviewSetAppPreviewsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def app_preview_sets_create_instance(request: web.Request, body) -> web.Response:
    """app_preview_sets_create_instance

    

    :param body: AppPreviewSet representation
    :type body: dict | bytes

    """
    body = AppPreviewSetCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_preview_sets_delete_instance(request: web.Request, id) -> web.Response:
    """app_preview_sets_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_preview_sets_get_instance(request: web.Request, id, fields_app_preview_sets=None, include=None, fields_app_previews=None, limit_app_previews=None) -> web.Response:
    """app_preview_sets_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_preview_sets: the fields to include for returned resources of type appPreviewSets
    :type fields_app_preview_sets: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_app_previews: the fields to include for returned resources of type appPreviews
    :type fields_app_previews: List[str]
    :param limit_app_previews: maximum number of related appPreviews returned (when they are included)
    :type limit_app_previews: int

    """
    return web.Response(status=200)
