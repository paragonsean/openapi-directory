# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_reward_earning_request import CreateRewardEarningRequest
from openapi_server.models.create_reward_earning_response import CreateRewardEarningResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_reward_earning_response import FetchRewardEarningResponse
from openapi_server.models.fetch_reward_earnings_response import FetchRewardEarningsResponse


pytestmark = pytest.mark.asyncio

async def test_create_reward_earning(client):
    """Test case for create_reward_earning

    Create a reward earning
    """
    body = openapi_server.CreateRewardEarningRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/reward_earning',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_reward_earning(client):
    """Test case for fetch_reward_earning

    Get a reward earning
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward_earning/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_reward_earnings(client):
    """Test case for fetch_reward_earnings

    List reward earnings
    """
    params = [('filter[groups]', 'filter_groups_example'),
                    ('filter[patient]', 'filter_patient_example'),
                    ('filter[ready_for_fulfillment]', True)]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward_earning',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

