# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accumulate_loyalty_points_request import AccumulateLoyaltyPointsRequest
from openapi_server.models.accumulate_loyalty_points_response import AccumulateLoyaltyPointsResponse
from openapi_server.models.adjust_loyalty_points_request import AdjustLoyaltyPointsRequest
from openapi_server.models.adjust_loyalty_points_response import AdjustLoyaltyPointsResponse
from openapi_server.models.calculate_loyalty_points_request import CalculateLoyaltyPointsRequest
from openapi_server.models.calculate_loyalty_points_response import CalculateLoyaltyPointsResponse
from openapi_server.models.create_loyalty_account_request import CreateLoyaltyAccountRequest
from openapi_server.models.create_loyalty_account_response import CreateLoyaltyAccountResponse
from openapi_server.models.create_loyalty_reward_request import CreateLoyaltyRewardRequest
from openapi_server.models.create_loyalty_reward_response import CreateLoyaltyRewardResponse
from openapi_server.models.delete_loyalty_reward_response import DeleteLoyaltyRewardResponse
from openapi_server.models.list_loyalty_programs_response import ListLoyaltyProgramsResponse
from openapi_server.models.redeem_loyalty_reward_request import RedeemLoyaltyRewardRequest
from openapi_server.models.redeem_loyalty_reward_response import RedeemLoyaltyRewardResponse
from openapi_server.models.retrieve_loyalty_account_response import RetrieveLoyaltyAccountResponse
from openapi_server.models.retrieve_loyalty_program_response import RetrieveLoyaltyProgramResponse
from openapi_server.models.retrieve_loyalty_reward_response import RetrieveLoyaltyRewardResponse
from openapi_server.models.search_loyalty_accounts_request import SearchLoyaltyAccountsRequest
from openapi_server.models.search_loyalty_accounts_response import SearchLoyaltyAccountsResponse
from openapi_server.models.search_loyalty_events_request import SearchLoyaltyEventsRequest
from openapi_server.models.search_loyalty_events_response import SearchLoyaltyEventsResponse
from openapi_server.models.search_loyalty_rewards_request import SearchLoyaltyRewardsRequest
from openapi_server.models.search_loyalty_rewards_response import SearchLoyaltyRewardsResponse


pytestmark = pytest.mark.asyncio

async def test_accumulate_loyalty_points(client):
    """Test case for accumulate_loyalty_points

    AccumulateLoyaltyPoints
    """
    body = {"request_body":{"accumulate_points":{"order_id":"RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY"},"idempotency_key":"58b90739-c3e8-4b11-85f7-e636d48d72cb","location_id":"P034NEENMD09F"},"request_params":"?account_id=5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/loyalty/accounts/{account_id}/accumulate'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adjust_loyalty_points(client):
    """Test case for adjust_loyalty_points

    AdjustLoyaltyPoints
    """
    body = {"request_body":{"adjust_points":{"points":10,"reason":"Complimentary points"},"idempotency_key":"bc29a517-3dc9-450e-aa76-fae39ee849d1"},"request_params":"?account_id=5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/loyalty/accounts/{account_id}/adjust'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calculate_loyalty_points(client):
    """Test case for calculate_loyalty_points

    CalculateLoyaltyPoints
    """
    body = {"request_body":{"order_id":"RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY"},"request_params":"?program_id=d619f755-2d17-41f3-990d-c04ecedd64dd"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/loyalty/programs/{program_id}/calculate'.format(program_id='program_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_loyalty_account(client):
    """Test case for create_loyalty_account

    CreateLoyaltyAccount
    """
    body = {"request_body":{"idempotency_key":"ec78c477-b1c3-4899-a209-a4e71337c996","loyalty_account":{"mapping":{"phone_number":"+14155551234"},"program_id":"d619f755-2d17-41f3-990d-c04ecedd64dd"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/loyalty/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_loyalty_reward(client):
    """Test case for create_loyalty_reward

    CreateLoyaltyReward
    """
    body = {"request_body":{"idempotency_key":"18c2e5ea-a620-4b1f-ad60-7b167285e451","reward":{"loyalty_account_id":"5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd","order_id":"RFZfrdtm3mhO1oGzf5Cx7fEMsmGZY","reward_tier_id":"e1b39225-9da5-43d1-a5db-782cdd8ad94f"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/loyalty/rewards',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_loyalty_reward(client):
    """Test case for delete_loyalty_reward

    DeleteLoyaltyReward
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/loyalty/rewards/{reward_id}'.format(reward_id='reward_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_loyalty_programs(client):
    """Test case for list_loyalty_programs

    ListLoyaltyPrograms
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/loyalty/programs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redeem_loyalty_reward(client):
    """Test case for redeem_loyalty_reward

    RedeemLoyaltyReward
    """
    body = {"request_body":{"idempotency_key":"98adc7f7-6963-473b-b29c-f3c9cdd7d994","location_id":"P034NEENMD09F"},"request_params":"?reward_id=9f18ac21-233a-31c3-be77-b45840f5a810"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/loyalty/rewards/{reward_id}/redeem'.format(reward_id='reward_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_loyalty_account(client):
    """Test case for retrieve_loyalty_account

    RetrieveLoyaltyAccount
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/loyalty/accounts/{account_id}'.format(account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_loyalty_program(client):
    """Test case for retrieve_loyalty_program

    RetrieveLoyaltyProgram
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/loyalty/programs/{program_id}'.format(program_id='program_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_loyalty_reward(client):
    """Test case for retrieve_loyalty_reward

    RetrieveLoyaltyReward
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/loyalty/rewards/{reward_id}'.format(reward_id='reward_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_loyalty_accounts(client):
    """Test case for search_loyalty_accounts

    SearchLoyaltyAccounts
    """
    body = {"request_body":{"limit":10,"query":{"mappings":[{"phone_number":"+14155551234"}]}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/loyalty/accounts/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_loyalty_events(client):
    """Test case for search_loyalty_events

    SearchLoyaltyEvents
    """
    body = {"request_body":{"limit":30,"query":{"filter":{"order_filter":{"order_id":"PyATxhYLfsMqpVkcKJITPydgEYfZY"}}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/loyalty/events/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_loyalty_rewards(client):
    """Test case for search_loyalty_rewards

    SearchLoyaltyRewards
    """
    body = {"request_body":{"limit":10,"query":{"loyalty_account_id":"5adcb100-07f1-4ee7-b8c6-6bb9ebc474bd"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/loyalty/rewards/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

