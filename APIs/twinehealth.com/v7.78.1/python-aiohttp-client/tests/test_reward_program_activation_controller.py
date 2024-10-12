# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_reward_program_activation_request import CreateRewardProgramActivationRequest
from openapi_server.models.create_reward_program_activation_response import CreateRewardProgramActivationResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_reward_program_activation_response import FetchRewardProgramActivationResponse
from openapi_server.models.fetch_reward_program_activations_response import FetchRewardProgramActivationsResponse


pytestmark = pytest.mark.asyncio

async def test_create_reward_program_activation(client):
    """Test case for create_reward_program_activation

    Create a reward program activation
    """
    body = openapi_server.CreateRewardProgramActivationRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/reward_program_activation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_reward_program_activation(client):
    """Test case for fetch_reward_program_activation

    Get a reward program activation
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward_program_activation/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_reward_program_activations(client):
    """Test case for fetch_reward_program_activations

    List reward program activations
    """
    params = [('filter[patient]', 'filter_patient_example'),
                    ('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward_program_activation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

