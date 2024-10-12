# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_translation_request import APIIPagedResponseGlobalResourcesSharedModelsTranslationRequest
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_translation_request import GlobalResourcesSharedModelsTranslationRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_requests_create_translation_request(client):
    """Test case for translation_requests_create_translation_request

    Create a translation request. Accepts a TranslationRequest object. Returns the Id of the created object. The state of the TranslationRequest must be ‘NotSubmitted’.
    """
    body = openapi_server.GlobalResourcesSharedModelsTranslationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/TranslationRequests',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translation_requests_get_translation_request(client):
    """Test case for translation_requests_get_translation_request

    Get a TranslationRequest object by id. Returns TranslationRequest object with its language ids and string ids.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/TranslationRequests/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translation_requests_get_translation_requests(client):
    """Test case for translation_requests_get_translation_requests

    Get all TranslationRequest objects. Returns a PagedResponse of TranslationRequest objects with their language ids and string ids.
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/TranslationRequests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_requests_update_translation_request(client):
    """Test case for translation_requests_update_translation_request

    Update a TranslationRequest object by id. Accepts a TranslationRequest object.
    """
    body = openapi_server.GlobalResourcesSharedModelsTranslationRequest()
    params = [('doResendRequest', True)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/TranslationRequests/{id}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_translation_requests_update_translation_request_strings(client):
    """Test case for translation_requests_update_translation_request_strings

    No Documentation Found.
    """
    body = ['body_example']
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/TranslationRequests/{id}/Strings'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

