# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_reward_earning_fulfillment_request import CreateRewardEarningFulfillmentRequest
from openapi_server.models.create_reward_earning_fulfillment_response import CreateRewardEarningFulfillmentResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_reward_earning_fulfillment_response import FetchRewardEarningFulfillmentResponse
from openapi_server.models.fetch_reward_earning_fulfillments_response import FetchRewardEarningFulfillmentsResponse


pytestmark = pytest.mark.asyncio

async def test_create_reward_earning_fulfillment(client):
    """Test case for create_reward_earning_fulfillment

    Create a reward earning fulfillment
    """
    body = openapi_server.CreateRewardEarningFulfillmentRequest()
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json',
    }
    response = await client.request(
        method='POST',
        path='/pub/reward_earning_fulfillment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_reward_earning_fulfillment(client):
    """Test case for fetch_reward_earning_fulfillment

    Get a reward earning fulfillment
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward_earning_fulfillment/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_reward_earning_fulfillments(client):
    """Test case for fetch_reward_earning_fulfillments

    List reward earning fulfillments
    """
    params = [('filter[patient]', 'filter_patient_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/reward_earning_fulfillment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

