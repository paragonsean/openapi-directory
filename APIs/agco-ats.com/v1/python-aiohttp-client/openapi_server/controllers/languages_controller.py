from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_language import APIIPagedResponseGlobalResourcesSharedModelsLanguage
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_language import GlobalResourcesSharedModelsLanguage
from openapi_server import util


async def languages_create_language(request: web.Request, body) -> web.Response:
    """Add a Language to support for translations. Accepts a Language object. Returns the Id of the created object.

    No Documentation Found.

    :param body: 
    :type body: dict | bytes

    """
    body = GlobalResourcesSharedModelsLanguage.from_dict(body)
    return web.Response(status=200)


async def languages_delete_language(request: web.Request, locale_id) -> web.Response:
    """Remove a Language from those supported for translations. Marks language as deleted.

    No Documentation Found.

    :param locale_id: 
    :type locale_id: int

    """
    return web.Response(status=200)


async def languages_get_language(request: web.Request, locale_id) -> web.Response:
    """Get a language by its id. Returns a Language object

    No Documentation Found.

    :param locale_id: 
    :type locale_id: int

    """
    return web.Response(status=200)


async def languages_get_languages(request: web.Request, limit=None, offset=None, include_deleted=None) -> web.Response:
    """Get a list of the languages for which translations are supported. Returns a PagedResponse of Language objects.

    No Documentation Found.

    :param limit: limit the number of Language objects returned. Optional (defaults to 10).
    :type limit: int
    :param offset: the number of Language objects to skip. Optional (defaults to 0).
    :type offset: int
    :param include_deleted: whether to include languages marked as deleted. Defaults to false
    :type include_deleted: bool

    """
    return web.Response(status=200)


async def languages_update_language(request: web.Request, locale_id, body) -> web.Response:
    """Update a language’s description. Accepts a Language object.

    No Documentation Found.

    :param locale_id: 
    :type locale_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GlobalResourcesSharedModelsLanguage.from_dict(body)
    return web.Response(status=200)
