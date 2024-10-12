# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_oas_support_shared_models_translation_key import APIIPagedResponseOASSupportSharedModelsTranslationKey
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.oas_support_shared_models_translation_key import OASSupportSharedModelsTranslationKey


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_keys_create_translation_key(client):
    """Test case for translation_keys_create_translation_key

    Create a translationKey object.
    """
    body = openapi_server.OASSupportSharedModelsTranslationKey()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/TranslationKeys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translation_keys_get(client):
    """Test case for translation_keys_get

    Get a paged response of TranslationKeys.
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('keyNames', 'key_names_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/TranslationKeys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translation_keys_get_translation_key(client):
    """Test case for translation_keys_get_translation_key

    Get TranslationKey by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/TranslationKeys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_keys_update_translation_key(client):
    """Test case for translation_keys_update_translation_key

    Update the StringID of the translationKey object.
    """
    body = openapi_server.OASSupportSharedModelsTranslationKey()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/TranslationKeys/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

