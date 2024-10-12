# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_language import APIIPagedResponseGlobalResourcesSharedModelsLanguage
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_language import GlobalResourcesSharedModelsLanguage


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_languages_create_language(client):
    """Test case for languages_create_language

    Add a Language to support for translations. Accepts a Language object. Returns the Id of the created object.
    """
    body = openapi_server.GlobalResourcesSharedModelsLanguage()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/Languages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_languages_delete_language(client):
    """Test case for languages_delete_language

    Remove a Language from those supported for translations. Marks language as deleted.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/Languages/{locale_id}'.format(locale_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_languages_get_language(client):
    """Test case for languages_get_language

    Get a language by its id. Returns a Language object
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Languages/{locale_id}'.format(locale_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_languages_get_languages(client):
    """Test case for languages_get_languages

    Get a list of the languages for which translations are supported. Returns a PagedResponse of Language objects.
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('includeDeleted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Languages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_languages_update_language(client):
    """Test case for languages_update_language

    Update a language’s description. Accepts a Language object.
    """
    body = openapi_server.GlobalResourcesSharedModelsLanguage()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/Languages/{locale_id}'.format(locale_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

