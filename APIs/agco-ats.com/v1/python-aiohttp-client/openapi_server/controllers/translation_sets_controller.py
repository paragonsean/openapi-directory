from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_translation_set import APIIPagedResponseGlobalResourcesSharedModelsTranslationSet
from openapi_server.models.apii_paged_response_global_resources_shared_models_translation_set_attribute import APIIPagedResponseGlobalResourcesSharedModelsTranslationSetAttribute
from openapi_server.models.apii_paged_response_global_resources_shared_models_translation_set_source_string import APIIPagedResponseGlobalResourcesSharedModelsTranslationSetSourceString
from openapi_server.models.apii_paged_response_global_resources_shared_models_translation_set_string import APIIPagedResponseGlobalResourcesSharedModelsTranslationSetString
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_translation_set import GlobalResourcesSharedModelsTranslationSet
from openapi_server.models.global_resources_shared_models_translation_set_attribute import GlobalResourcesSharedModelsTranslationSetAttribute
from openapi_server.models.global_resources_shared_models_translation_set_statistics import GlobalResourcesSharedModelsTranslationSetStatistics
from openapi_server.models.global_resources_shared_models_translation_set_string import GlobalResourcesSharedModelsTranslationSetString
from openapi_server import util


async def translation_sets_delete_translation_set_attribute(request: web.Request, id) -> web.Response:
    """Delete a set of TranslationSetAttribute object

    No Documentation Found.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def translation_sets_get_source_strings(request: web.Request, id, limit=None, offset=None) -> web.Response:
    """Gets the information needed to translate a string in a translation set

    No Documentation Found.

    :param id: 
    :type id: int
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def translation_sets_get_statistics(request: web.Request, id) -> web.Response:
    """Gets the statistics for translation sets such as the language ids and count of string definitions.

    No Documentation Found.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def translation_sets_get_translation_set(request: web.Request, id, include_attributes=None) -> web.Response:
    """Get a TranslationSet object by its id. Related TranslationSetStrings are NOT returned.

    No Documentation Found.

    :param id: 
    :type id: int
    :param include_attributes: Names of Attributes to include when retrieving this Translation set. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included.
    :type include_attributes: str

    """
    return web.Response(status=200)


async def translation_sets_get_translation_set_attributes(request: web.Request, id, limit=None, offset=None, name=None) -> web.Response:
    """Get a PagedResponse of TranslationSetAttribute objects

    No Documentation Found.

    :param id: 
    :type id: int
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def translation_sets_get_translation_set_strings(request: web.Request, id, limit=None, offset=None) -> web.Response:
    """Get a PagedResponse of TranslationSetString objects

    No Documentation Found.

    :param id: 
    :type id: int
    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int

    """
    return web.Response(status=200)


async def translation_sets_get_translation_sets(request: web.Request, limit=None, offset=None, translation_request_id=None, state=None, string_id=None, language_id=None, include_attributes=None) -> web.Response:
    """Get a PagedResponse of TranslationSet objects. Related TranslationSetStrings are NOT returned

    No Documentation Found.

    :param limit: 
    :type limit: int
    :param offset: 
    :type offset: int
    :param translation_request_id: 
    :type translation_request_id: int
    :param state: 
    :type state: str
    :param string_id: 
    :type string_id: str
    :param language_id: 
    :type language_id: int
    :param include_attributes: Names of Attributes to include when retrieving this submission. This should be a comma-separated list. If not provided, Attributes are not included. If &#39;*&#39;, all Attributes are included.
    :type include_attributes: str

    """
    return web.Response(status=200)


async def translation_sets_post_translation_set_attribute(request: web.Request, id, body) -> web.Response:
    """Create a TranslationSetAttribute object

    No Documentation Found.

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GlobalResourcesSharedModelsTranslationSetAttribute.from_dict(body)
    return web.Response(status=200)


async def translation_sets_post_translation_set_attributes(request: web.Request, id, body) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param id: 
    :type id: int
    :param body: 
    :type body: list | bytes

    """
    body = [GlobalResourcesSharedModelsTranslationSetAttribute.from_dict(d) for d in body]
    return web.Response(status=200)


async def translation_sets_update_translation_set(request: web.Request, id, body) -> web.Response:
    """Update a Translation Set. Accepts a TranslationSet object. Only the state property may be updated.

    No Documentation Found.

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GlobalResourcesSharedModelsTranslationSet.from_dict(body)
    return web.Response(status=200)


async def translation_sets_update_translation_set_attribute(request: web.Request, id, body) -> web.Response:
    """Update a TranslationSetAttribute object

    No Documentation Found.

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GlobalResourcesSharedModelsTranslationSetAttribute.from_dict(body)
    return web.Response(status=200)


async def translation_sets_update_translation_set_attributes(request: web.Request, body) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param body: 
    :type body: list | bytes

    """
    body = [GlobalResourcesSharedModelsTranslationSetAttribute.from_dict(d) for d in body]
    return web.Response(status=200)


async def translation_sets_update_translation_set_strings(request: web.Request, id, body) -> web.Response:
    """No Documentation Found.

    No Documentation Found.

    :param id: 
    :type id: int
    :param body: 
    :type body: list | bytes

    """
    body = [GlobalResourcesSharedModelsTranslationSetString.from_dict(d) for d in body]
    return web.Response(status=200)
