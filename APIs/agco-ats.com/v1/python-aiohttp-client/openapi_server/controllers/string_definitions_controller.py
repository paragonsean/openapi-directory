from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_string_definition import APIIPagedResponseGlobalResourcesSharedModelsStringDefinition
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_string_definition import GlobalResourcesSharedModelsStringDefinition
from openapi_server import util


async def string_definitions_get_definition(request: web.Request, id, include_translations=None, include_deleted_languages=None, language_ids=None) -> web.Response:
    """Get a paged response of Global String Definitions.

    No Documentation Found.

    :param id: 
    :type id: str
    :param include_translations: Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.
    :type include_translations: bool
    :param include_deleted_languages: Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.
    :type include_deleted_languages: bool
    :param language_ids: Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.
    :type language_ids: str

    """
    return web.Response(status=200)


async def string_definitions_get_definitions(request: web.Request, limit=None, modified_after_timestamp=None, include_translations=None, string_text=None, description_text=None, use_full_text=None, include_deleted_languages=None, language_ids=None, string_ids=None, matching_translations_only=None) -> web.Response:
    """Get a paged response of Global String Definitions.

    No Documentation Found.

    :param limit: Optional. The page limit. The default page limit is 10. Ignored if &#39;stringIds&#39; is provided.
    :type limit: int
    :param modified_after_timestamp: Optional. Return only the StringDefinition objects that have a Timestamp value greater than that provided. This will be an encoded byte array.
    :type modified_after_timestamp: str
    :param include_translations: Optional. Indicates whether to include the StringTranslations for the StringDefinition. Defaults to false.
    :type include_translations: bool
    :param string_text: Optional. The text for which to search in the StringDefinition object’s translations. Only StringDefinition objects for matching StringTranslation objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards. includeTranslations must be true.
    :type string_text: str
    :param description_text: Optional. The text for which to search in the StringDefinition description field. Only matching objects are returned. Does not filter if no value is provided. Supports beginning and/or ending wildcards.
    :type description_text: str
    :param use_full_text: Optional. This flag is used to determin whether to use the FullText Search or not.
    :type use_full_text: bool
    :param include_deleted_languages: Optional. Indicates whether to include languages marked as deleted. includeTranslations must be true. Defaults to false.
    :type include_deleted_languages: bool
    :param language_ids: Optional. A comma-delimited list of language ids. Only StringTranslation objects with a matching language id will be returned. Optional. By default all locales are returned. includeTranslations must be true. The StringDefinition is still returned even if the filtered translations list is empty.
    :type language_ids: str
    :param string_ids: Optional. A comma-delimited list of string ids. Up to 40 string IDs may be provided. May not be used with &#39;modifiedAfterTimestamp&#39;, &#39;stringText&#39;, &#39;descriptionText&#39;, or &#39;useFullText&#39;.
    :type string_ids: str
    :param matching_translations_only: Optional. If false, all translations for returned String Definitions are included. Must be used with &#39;stringText&#39; provided and &#39;includeTranslations&#39; &#x3D; true.
    :type matching_translations_only: bool

    """
    return web.Response(status=200)


async def string_definitions_post_definition(request: web.Request, body) -> web.Response:
    """Create StringDefinition object. The originating translation must be provided. Accepts an array of StringDefinition objects. Returns nothing.

    No Documentation Found.

    :param body: The StringDefinition Object array, along with originating translation.
    :type body: list | bytes

    """
    body = [GlobalResourcesSharedModelsStringDefinition.from_dict(d) for d in body]
    return web.Response(status=200)


async def string_definitions_update_definitions(request: web.Request, body) -> web.Response:
    """Update StringDefinition objects. Accepts an array of StringDefinition objects. This endpoint will add StringDefinitionChange objects to the database. The DescriptionForTranslator may not be modified after a String is submitted for translation.

    No Documentation Found.

    :param body: The Array of Definitions to update
    :type body: list | bytes

    """
    body = [GlobalResourcesSharedModelsStringDefinition.from_dict(d) for d in body]
    return web.Response(status=200)
