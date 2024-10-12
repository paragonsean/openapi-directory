# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_build_system_shared_dto_step import APIPagedResponseBuildSystemSharedDTOStep
from openapi_server.models.build_system_shared_dto_step import BuildSystemSharedDTOStep


pytestmark = pytest.mark.asyncio

async def test_steps_get_step(client):
    """Test case for steps_get_step

    Get a Step by ID
    """
    params = [('isIncludeDeleted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/steps/{step_id}'.format(step_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_steps_get_steps(client):
    """Test case for steps_get_steps

    Get Steps
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('includeDeleted', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/steps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_steps_post_step(client):
    """Test case for steps_post_step

    Create a Step
    """
    body = openapi_server.BuildSystemSharedDTOStep()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/steps',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_steps_put_step(client):
    """Test case for steps_put_step

    Update a Step
    """
    body = openapi_server.BuildSystemSharedDTOStep()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/steps/{step_id}'.format(step_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

