from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_oas_support_shared_models_translation_key import APIIPagedResponseOASSupportSharedModelsTranslationKey
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.oas_support_shared_models_translation_key import OASSupportSharedModelsTranslationKey
from openapi_server import util


async def translation_keys_create_translation_key(request: web.Request, body) -> web.Response:
    """Create a translationKey object.

    No Documentation Found.

    :param body: 
    :type body: dict | bytes

    """
    body = OASSupportSharedModelsTranslationKey.from_dict(body)
    return web.Response(status=200)


async def translation_keys_get(request: web.Request, limit=None, offset=None, key_names=None) -> web.Response:
    """Get a paged response of TranslationKeys.

    

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int
    :param key_names: Can filter by keyNames, a comma deliminated list.
    :type key_names: str

    """
    return web.Response(status=200)


async def translation_keys_get_translation_key(request: web.Request, id) -> web.Response:
    """Get TranslationKey by ID

    No Documentation Found.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def translation_keys_update_translation_key(request: web.Request, id, body) -> web.Response:
    """Update the StringID of the translationKey object.

    No Documentation Found.

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = OASSupportSharedModelsTranslationKey.from_dict(body)
    return web.Response(status=200)
