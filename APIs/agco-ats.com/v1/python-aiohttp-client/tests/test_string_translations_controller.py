# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_string_translation import APIIPagedResponseGlobalResourcesSharedModelsStringTranslation
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_string_translation import GlobalResourcesSharedModelsStringTranslation


pytestmark = pytest.mark.asyncio

async def test_string_translations_get_translation(client):
    """Test case for string_translations_get_translation

    Get a single translation based upon stringId and languageId
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/StringTranslations/{string_id}/{language_id}'.format(string_id='string_id_example', language_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_string_translations_get_translations(client):
    """Test case for string_translations_get_translations

    Get a paged response of Global String Translations.
    """
    params = [('limit', 56),
                    ('modifiedAfterTimestamp', 'modified_after_timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/StringTranslations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_string_translations_update_translation(client):
    """Test case for string_translations_update_translation

    Update a string value or a state for a string translation.
    """
    body = openapi_server.GlobalResourcesSharedModelsStringTranslation()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/StringTranslations/{string_id}/{language_id}'.format(string_id='string_id_example', language_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_string_translations_update_translations(client):
    """Test case for string_translations_update_translations

    Update corrections to string translations
    """
    body = [openapi_server.GlobalResourcesSharedModelsStringTranslation()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/StringTranslations/Batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

