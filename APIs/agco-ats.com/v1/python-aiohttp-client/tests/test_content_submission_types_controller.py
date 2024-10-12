# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.content_submission_shared_business_entities_content_submission_type import ContentSubmissionSharedBusinessEntitiesContentSubmissionType


pytestmark = pytest.mark.asyncio

async def test_content_submission_types_delete_content_submission_type(client):
    """Test case for content_submission_types_delete_content_submission_type

    Remove a Content Submission Type
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/ContentSubmissionTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_submission_types_get_content_submission_type(client):
    """Test case for content_submission_types_get_content_submission_type

    Retrieves a Content Submission Type by its ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentSubmissionTypes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_submission_types_get_content_submission_types(client):
    """Test case for content_submission_types_get_content_submission_types

    Returns available Content Submission Types.
    """
    params = [('enabled', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/ContentSubmissionTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_submission_types_post_content_submission_type(client):
    """Test case for content_submission_types_post_content_submission_type

    Add a Content Submission Type
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentSubmissionType()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/ContentSubmissionTypes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_content_submission_types_put_content_submission_type(client):
    """Test case for content_submission_types_put_content_submission_type

    Update a Content Submission Type
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesContentSubmissionType()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/ContentSubmissionTypes/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

