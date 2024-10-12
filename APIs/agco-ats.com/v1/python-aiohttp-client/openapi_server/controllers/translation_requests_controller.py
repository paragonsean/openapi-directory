from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_translation_request import APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_translation_request import GlobalResourcesSharedModelsTranslationRequest
from openapi_server import util


async def translation_requests_create_translation_request(request: web.Request, body) -> web.Response:
    """Create a translation request. Accepts a TranslationRequest object. Returns the Id of the created object. The state of the TranslationRequest must be ‘NotSubmitted’.

    No Documentation Found.

    :param body: 
    :type body: dict | bytes

    """
    body = GlobalResourcesSharedModelsTranslationRequest.from_dict(body)
    return web.Response(status=200)


async def translation_requests_get_translation_request(request: web.Request, id) -> web.Response:
    """Get a TranslationRequest object by id. Returns TranslationRequest object with its language ids and string ids.

    No Documentation Found.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def translation_requests_get_translation_requests(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get all TranslationRequest objects. Returns a PagedResponse of TranslationRequest objects with their language ids and string ids.

    No Documentation Found.

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def translation_requests_update_translation_request(request: web.Request, id, body, do_resend_request=None) -> web.Response:
    """Update a TranslationRequest object by id. Accepts a TranslationRequest object.

    No Documentation Found.

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes
    :param do_resend_request: 
    :type do_resend_request: bool

    """
    body = GlobalResourcesSharedModelsTranslationRequest.from_dict(body)
    return web.Response(status=200)


async def translation_requests_update_translation_request_strings(request: web.Request, id, body) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param id: 
    :type id: int
    :param body: 
    :type body: List[str]

    """
    return web.Response(status=200)
