# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_content_submission_shared_business_entities_user_content_definition import APIPagedResponseContentSubmissionSharedBusinessEntitiesUserContentDefinition
from openapi_server.models.content_submission_shared_business_entities_user_content_definition import ContentSubmissionSharedBusinessEntitiesUserContentDefinition


pytestmark = pytest.mark.asyncio

async def test_user_content_definitions_delete_user_content_definition(client):
    """Test case for user_content_definitions_delete_user_content_definition

    Delete a UserContentDefinition
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/UserContentDefinitions/{user_content_definition_id}'.format(user_content_definition_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_content_definitions_get_user_content_definition(client):
    """Test case for user_content_definitions_get_user_content_definition

    Get a UserContentDefinition by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/UserContentDefinitions/{user_content_definition_id}'.format(user_content_definition_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_content_definitions_get_user_content_definitions(client):
    """Test case for user_content_definitions_get_user_content_definitions

    Get UserContentDefinitions
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('userID', 56),
                    ('contentDefinitionID', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/UserContentDefinitions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_user_content_definitions_post_user_content_definition(client):
    """Test case for user_content_definitions_post_user_content_definition

    Create a UserContentDefinition
    """
    body = openapi_server.ContentSubmissionSharedBusinessEntitiesUserContentDefinition()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/UserContentDefinitions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

