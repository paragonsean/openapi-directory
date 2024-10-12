from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_string_translation import APIIPagedResponseGlobalResourcesSharedModelsStringTranslation
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_string_translation import GlobalResourcesSharedModelsStringTranslation
from openapi_server import util


async def string_translations_get_translation(request: web.Request, string_id, language_id) -> web.Response:
    """Get a single translation based upon stringId and languageId

    No Documentation Found.

    :param string_id: 
    :type string_id: str
    :param language_id: 
    :type language_id: int

    """
    return web.Response(status=200)


async def string_translations_get_translations(request: web.Request, limit=None, modified_after_timestamp=None) -> web.Response:
    """Get a paged response of Global String Translations.

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param modified_after_timestamp: Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.
    :type modified_after_timestamp: str

    """
    return web.Response(status=200)


async def string_translations_update_translation(request: web.Request, string_id, language_id, body) -> web.Response:
    """Update a string value or a state for a string translation.

    No Documentation Found.

    :param string_id: 
    :type string_id: str
    :param language_id: 
    :type language_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GlobalResourcesSharedModelsStringTranslation.from_dict(body)
    return web.Response(status=200)


async def string_translations_update_translations(request: web.Request, body) -> web.Response:
    """Update corrections to string translations

    No Documentation Found.

    :param body: 
    :type body: list | bytes

    """
    body = [GlobalResourcesSharedModelsStringTranslation.from_dict(d) for d in body]
    return web.Response(status=200)
