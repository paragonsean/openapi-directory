from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_operation_status import AsyncOperationStatus
from openapi_server.models.client_strings import ClientStrings
from openapi_server.models.continuous_project_cache import ContinuousProjectCache
from openapi_server.models.continuous_project_document_strings_body import ContinuousProjectDocumentStringsBody
from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.string_list import StringList
from openapi_server.models.translation_memory_unit import TranslationMemoryUnit
from openapi_server import util


async def clear_translation_cache(request: web.Request, project_id, locale=None, file_id=None) -> web.Response:
    """Clear translation cache

    Clear/delete continuous project translation cache.

    :param project_id: Project ID
    :type project_id: int
    :param locale: Locale
    :type locale: str
    :param file_id: Continuous Project File ID
    :type file_id: int

    """
    return web.Response(status=200)


async def get_continuous_project_file_strings(request: web.Request, project_id, document_id) -> web.Response:
    """View strings their translations in a continuous document

    View the strings from a document and their translations in your continuous translation project, for all target languages. If you need the translated version of your source document/file, then you need to use package and download endpoints.

    :param project_id: Project ID
    :type project_id: int
    :param document_id: Document ID/Name
    :type document_id: int

    """
    return web.Response(status=200)


async def get_continuous_project_strings(request: web.Request, project_id) -> web.Response:
    """View strings and translations in continuous project

    View the strings and their translations in your continuous translation project, for all target languages. If you need the translated version of your source document/file, then you need to use package and download endpoints.

    :param project_id: Project ID
    :type project_id: int

    """
    return web.Response(status=200)


async def get_document_translations(request: web.Request, project_id, document_id) -> web.Response:
    """View strings and translations of a document

    View the strings and their translations in your translation project for the specified source document. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

    :param project_id: Project ID
    :type project_id: int
    :param document_id: Document ID
    :type document_id: int

    """
    return web.Response(status=200)


async def get_document_translations_for_language(request: web.Request, project_id, document_id, language) -> web.Response:
    """View strings and translations of a document for target language

    View the strings and their translations in the given target language for the specified source document. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

    :param project_id: Project ID
    :type project_id: int
    :param document_id: Document ID
    :type document_id: int
    :param language: Target language code.
    :type language: str

    """
    return web.Response(status=200)


async def get_project_strings(request: web.Request, project_id) -> web.Response:
    """View project strings and translations

    View the strings and their translations in your translation project, for all target languages. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

    :param project_id: Project ID
    :type project_id: int

    """
    return web.Response(status=200)


async def get_project_strings_for_language(request: web.Request, project_id, language) -> web.Response:
    """View strings and translations for target language

    View the strings and their translations in your translation project for the specified target language. The list of translations is live if your project is not completed yet. If you need the translated version of your source document/file, then you need to use package and download endpoints.

    :param project_id: Project ID
    :type project_id: int
    :param language: Target language code
    :type language: str

    """
    return web.Response(status=200)


async def get_project_translations(request: web.Request, project_id) -> web.Response:
    """Deprecated. Use /projects/{projectId}/strings instead.

    

    :param project_id: Project ID
    :type project_id: int

    """
    return web.Response(status=200)


async def get_project_translations_for_language(request: web.Request, project_id, language) -> web.Response:
    """Deprecated. use /projects/{projectId}/strings/{language} instead.

    

    :param project_id: Project ID
    :type project_id: int
    :param language: Target language code
    :type language: str

    """
    return web.Response(status=200)


async def get_strings(request: web.Request, source_language=None, page=None) -> web.Response:
    """View account strings (translation memory)

    Get a list of all strings and their translations under your account, from all projects. This is your MotaWord translation memory. If you have the related permission, this endpoint will also return strings from your company account.

    :param source_language: Source Language Code
    :type source_language: str
    :param page: Requested page
    :type page: int

    """
    return web.Response(status=200)


async def get_translation_cache(request: web.Request, project_id, flatten=None) -> web.Response:
    """View cached strings translations in continuous project

    MotaWord caches your account intensively (and in a smart way) in real-time translation environments. This endpoint will return the currently cached strings and translations in your continuous translation project.

    :param project_id: Project ID
    :type project_id: int
    :param flatten: Flatten cache results and ignore document keys
    :type flatten: bool

    """
    return web.Response(status=200)


async def package_project_translation_memory(request: web.Request, project_id, _async=None, format=None) -> web.Response:
    """Download project translation memory

    Package and download project translation memory in TMX format

    :param project_id: Project ID
    :type project_id: int
    :param _async: If you want to package and download the translation memory synchronously, mark this parameter as &#39;0&#39;. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call.
    :type _async: int
    :param format: Translation Memory file format
    :type format: str

    """
    return web.Response(status=200)


async def package_project_translation_memory_for_language(request: web.Request, project_id, language_code, _async=None, format=None) -> web.Response:
    """Download language-specific project translation memory

    Package and download project translation memory in TMX format for a specific target language.

    :param project_id: Project ID
    :type project_id: int
    :param language_code: Language Code
    :type language_code: str
    :param _async: If you want to package and download the translation memory synchronously, mark this parameter as &#39;0&#39;. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call.
    :type _async: int
    :param format: Translation Memory file format
    :type format: str

    """
    return web.Response(status=200)


async def package_project_translation_memory_for_language_status(request: web.Request, project_id, language_code, async_request_key) -> web.Response:
    """Check language-specific translation memory packaging status

    Check translation memory packaging status for async packaging requests, using the key returned from strings/package call.

    :param project_id: Project ID
    :type project_id: int
    :param language_code: Language Code
    :type language_code: str
    :param async_request_key: Async operation key
    :type async_request_key: str

    """
    return web.Response(status=200)


async def package_project_translation_memory_status(request: web.Request, project_id, async_request_key) -> web.Response:
    """Check translation memory packaging status

    Check translation memory packaging status for async packaging requests, using the key returned from strings/package call.

    :param project_id: Project ID
    :type project_id: int
    :param async_request_key: Async operation key
    :type async_request_key: str

    """
    return web.Response(status=200)


async def package_user_translation_memory(request: web.Request, language_code, _async=None, email=None) -> web.Response:
    """Download account translation memory

    Package and download account translation memory in TMX format. If you have the related permission, this will also download your company translation memory.

    :param language_code: Source Language Code
    :type language_code: str
    :param _async: If you want to package and download the translation memory synchronously, mark this parameter as &#39;0&#39;. It will package the translation memory and then return the packaged file in the response, identical to async/download call after an asynchronous /package call.
    :type _async: int
    :param email: If you don&#39;t need us to email the TMX, set this to &#39;0&#39;. Default is 1.
    :type email: int

    """
    return web.Response(status=200)


async def package_user_translation_memory_for_language_status(request: web.Request, language_code, async_request_key) -> web.Response:
    """Check account translation memory packaging status

    Check translation memory packaging status for async packaging requests, using the key returned from strings/package call.

    :param language_code: Language Code
    :type language_code: str
    :param async_request_key: Async operation key
    :type async_request_key: str

    """
    return web.Response(status=200)


async def post_continuous_project_file_strings(request: web.Request, project_id, body=None) -> web.Response:
    """Get a list of strings and its translations in the project.

    

    :param project_id: Project ID
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ContinuousProjectDocumentStringsBody.from_dict(body)
    return web.Response(status=200)


async def recache_translations(request: web.Request, project_id, locale=None, file_id=None) -> web.Response:
    """Recache translations

    Recache translations for the continuous project.

    :param project_id: Project ID
    :type project_id: int
    :param locale: Locale
    :type locale: str
    :param file_id: Continuous Project File ID
    :type file_id: int

    """
    return web.Response(status=200)


async def update_translation_memory_unit(request: web.Request, body=None) -> web.Response:
    """Update string translation

    Update the translation of a string from your account strings/translation memory.

    :param body: 
    :type body: dict | bytes

    """
    body = TranslationMemoryUnit.from_dict(body)
    return web.Response(status=200)
