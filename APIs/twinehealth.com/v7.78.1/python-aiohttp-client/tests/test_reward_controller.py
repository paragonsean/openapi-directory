# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_reward_request import CreateRewardRequest
from openapi_server.models.create_reward_response import CreateRewardResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_reward_response import FetchRewardResponse
from openapi_server.models.fetch_rewards_response import FetchRewardsResponse


pytestmark = pytest.mark.asyncio

async def test_create_reward(client):
    """Test case for create_reward

    Create a reward
    """
    body = openapi_server.CreateRewardRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/reward',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_reward(client):
    """Test case for fetch_reward

    Get a reward
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_rewards(client):
    """Test case for fetch_rewards

    List rewards
    """
    params = [('filter[patient]', 'filter_patient_example'),
                    ('filter[reward_program_activation]', 'filter_reward_program_activation_example'),
                    ('filter[thread]', 'filter_thread_example'),
                    ('filter[groups]', 'filter_groups_example'),
                    ('filter[organization]', 'filter_organization_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

