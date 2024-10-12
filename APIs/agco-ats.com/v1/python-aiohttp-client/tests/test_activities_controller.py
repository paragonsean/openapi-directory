# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_activity import APIPagedResponseBuildSystemSharedDTOActivity
from openapi_server.models.build_system_shared_dto_activity import BuildSystemSharedDTOActivity


pytestmark = pytest.mark.asyncio

async def test_activities_delete_activity(client):
    """Test case for activities_delete_activity

    Mark the delete flag for the Activity
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/activities/{activity_id}'.format(activity_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_get_activities(client):
    """Test case for activities_get_activities

    Get Activities
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('isIncludeDeleted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/activities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_get_activity(client):
    """Test case for activities_get_activity

    Get an Activity by ID
    """
    params = [('isIncludeDeleted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/activities/{activity_id}'.format(activity_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_activities_post_activity(client):
    """Test case for activities_post_activity

    Create an Activity
    """
    body = openapi_server.BuildSystemSharedDTOActivity()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/activities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_activities_put_activity(client):
    """Test case for activities_put_activity

    Update an Activity
    """
    body = openapi_server.BuildSystemSharedDTOActivity()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/activities/{activity_id}'.format(activity_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

