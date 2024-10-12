# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_operation_status import AsyncOperationStatus
from openapi_server.models.client_strings import ClientStrings
from openapi_server.models.continuous_project_cache import ContinuousProjectCache
from openapi_server.models.continuous_project_document_strings_body import ContinuousProjectDocumentStringsBody
from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.string_list import StringList
from openapi_server.models.translation_memory_unit import TranslationMemoryUnit


pytestmark = pytest.mark.asyncio

async def test_clear_translation_cache(client):
    """Test case for clear_translation_cache

    Clear translation cache
    """
    params = [('locale', 'locale_example'),
                    ('file_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/continuous_projects/{project_id}/strings/cached'.format(project_id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continuous_project_file_strings(client):
    """Test case for get_continuous_project_file_strings

    View strings their translations in a continuous document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{project_id}/documents/{document_id}/strings'.format(project_id=74, document_id=179469),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continuous_project_strings(client):
    """Test case for get_continuous_project_strings

    View strings and translations in continuous project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{project_id}/strings'.format(project_id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_document_translations(client):
    """Test case for get_document_translations

    View strings and translations of a document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/documents/{document_id}/translations'.format(project_id=74, document_id=179469),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_document_translations_for_language(client):
    """Test case for get_document_translations_for_language

    View strings and translations of a document for target language
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/documents/{document_id}/translations/{language}'.format(project_id=74, document_id=179469, language='en-US'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_strings(client):
    """Test case for get_project_strings

    View project strings and translations
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/strings'.format(project_id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_strings_for_language(client):
    """Test case for get_project_strings_for_language

    View strings and translations for target language
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/strings/{language}'.format(project_id=74, language='en-US'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_translations(client):
    """Test case for get_project_translations

    Deprecated. Use /projects/{projectId}/strings instead.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/translations'.format(project_id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_translations_for_language(client):
    """Test case for get_project_translations_for_language

    Deprecated. use /projects/{projectId}/strings/{language} instead.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/translations/{language}'.format(project_id=74, language='en-US'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_strings(client):
    """Test case for get_strings

    View account strings (translation memory)
    """
    params = [('source_language', 'source_language_example'),
                    ('page', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/strings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_translation_cache(client):
    """Test case for get_translation_cache

    View cached strings translations in continuous project
    """
    params = [('flatten', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/continuous_projects/{project_id}/strings/cached'.format(project_id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_project_translation_memory(client):
    """Test case for package_project_translation_memory

    Download project translation memory
    """
    params = [('async', 0),
                    ('format', 'tmx')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{project_id}/strings/package'.format(project_id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_project_translation_memory_for_language(client):
    """Test case for package_project_translation_memory_for_language

    Download language-specific project translation memory
    """
    params = [('async', 0),
                    ('format', 'tmx')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{project_id}/strings/{language_code}/package'.format(project_id=74, language_code='en-US'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_project_translation_memory_for_language_status(client):
    """Test case for package_project_translation_memory_for_language_status

    Check language-specific translation memory packaging status
    """
    params = [('async_request_key', 'f0db2468-6b77-41a4-bafe-70157bc166ad')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/strings/{language_code}/package/status'.format(project_id=74, language_code='en-US'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_project_translation_memory_status(client):
    """Test case for package_project_translation_memory_status

    Check translation memory packaging status
    """
    params = [('async_request_key', 'f0db2468-6b77-41a4-bafe-70157bc166ad')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/strings/package/status'.format(project_id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_user_translation_memory(client):
    """Test case for package_user_translation_memory

    Download account translation memory
    """
    params = [('async', 0),
                    ('email', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/strings/{language_code}/package'.format(language_code='en-US'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_user_translation_memory_for_language_status(client):
    """Test case for package_user_translation_memory_for_language_status

    Check account translation memory packaging status
    """
    params = [('async_request_key', 'f0db2468-6b77-41a4-bafe-70157bc166ad')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/strings/{language_code}/package/status'.format(language_code='en-US'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_continuous_project_file_strings(client):
    """Test case for post_continuous_project_file_strings

    Get a list of strings and its translations in the project.
    """
    body = {"documentName":"documentName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{project_id}/documents/strings'.format(project_id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recache_translations(client):
    """Test case for recache_translations

    Recache translations
    """
    params = [('locale', 'locale_example'),
                    ('file_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/continuous_projects/{project_id}/strings/recache-tms'.format(project_id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_translation_memory_unit(client):
    """Test case for update_translation_memory_unit

    Update string translation
    """
    body = {"targetLanguage":"targetLanguage","sourceText":"sourceText","sourceLanguage":"sourceLanguage","targetText":"targetText"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/strings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

