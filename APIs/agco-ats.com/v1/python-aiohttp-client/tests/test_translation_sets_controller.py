# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_translation_sets_delete_translation_set_attribute(client):
    """Test case for translation_sets_delete_translation_set_attribute

    Delete a set of TranslationSetAttribute object
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/TranslationSetAttributes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translation_sets_get_source_strings(client):
    """Test case for translation_sets_get_source_strings

    Gets the information needed to translate a string in a translation set
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/TranslationSets/{id}/SourceStrings'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translation_sets_get_statistics(client):
    """Test case for translation_sets_get_statistics

    Gets the statistics for translation sets such as the language ids and count of string definitions.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/TranslationSets/{id}/Statistics'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translation_sets_get_translation_set(client):
    """Test case for translation_sets_get_translation_set

    Get a TranslationSet object by its id. Related TranslationSetStrings are NOT returned.
    """
    params = [('includeAttributes', 'include_attributes_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/TranslationSets/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translation_sets_get_translation_set_attributes(client):
    """Test case for translation_sets_get_translation_set_attributes

    Get a PagedResponse of TranslationSetAttribute objects
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/TranslationSets/{id}/Attributes'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translation_sets_get_translation_set_strings(client):
    """Test case for translation_sets_get_translation_set_strings

    Get a PagedResponse of TranslationSetString objects
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/TranslationSets/{id}/Strings'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translation_sets_get_translation_sets(client):
    """Test case for translation_sets_get_translation_sets

    Get a PagedResponse of TranslationSet objects. Related TranslationSetStrings are NOT returned
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('translationRequestID', 56),
                    ('state', 'state_example'),
                    ('stringId', 'string_id_example'),
                    ('languageId', 56),
                    ('includeAttributes', 'include_attributes_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/TranslationSets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_sets_post_translation_set_attribute(client):
    """Test case for translation_sets_post_translation_set_attribute

    Create a TranslationSetAttribute object
    """
    body = openapi_server.GlobalResourcesSharedModelsTranslationSetAttribute()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/TranslationSets/{id}/Attributes'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_sets_post_translation_set_attributes(client):
    """Test case for translation_sets_post_translation_set_attributes

    No Documentation Found.
    """
    body = [openapi_server.GlobalResourcesSharedModelsTranslationSetAttribute()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/TranslationSets/{id}/Attributes/Batch'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_sets_update_translation_set(client):
    """Test case for translation_sets_update_translation_set

    Update a Translation Set. Accepts a TranslationSet object. Only the state property may be updated.
    """
    body = openapi_server.GlobalResourcesSharedModelsTranslationSet()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/TranslationSets/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_sets_update_translation_set_attribute(client):
    """Test case for translation_sets_update_translation_set_attribute

    Update a TranslationSetAttribute object
    """
    body = openapi_server.GlobalResourcesSharedModelsTranslationSetAttribute()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/TranslationSetAttributes/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_sets_update_translation_set_attributes(client):
    """Test case for translation_sets_update_translation_set_attributes

    No Documentation Found.
    """
    body = [openapi_server.GlobalResourcesSharedModelsTranslationSetAttribute()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/TranslationSetAttributes/Batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_sets_update_translation_set_strings(client):
    """Test case for translation_sets_update_translation_set_strings

    No Documentation Found.
    """
    body = [openapi_server.GlobalResourcesSharedModelsTranslationSetString()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/TranslationSets/{id}/Strings'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

