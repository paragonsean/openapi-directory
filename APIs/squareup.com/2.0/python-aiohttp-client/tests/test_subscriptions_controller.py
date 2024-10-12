# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_subscription_response import CancelSubscriptionResponse
from openapi_server.models.create_subscription_request import CreateSubscriptionRequest
from openapi_server.models.create_subscription_response import CreateSubscriptionResponse
from openapi_server.models.list_subscription_events_response import ListSubscriptionEventsResponse
from openapi_server.models.resume_subscription_response import ResumeSubscriptionResponse
from openapi_server.models.retrieve_subscription_response import RetrieveSubscriptionResponse
from openapi_server.models.search_subscriptions_request import SearchSubscriptionsRequest
from openapi_server.models.search_subscriptions_response import SearchSubscriptionsResponse
from openapi_server.models.update_subscription_request import UpdateSubscriptionRequest
from openapi_server.models.update_subscription_response import UpdateSubscriptionResponse


pytestmark = pytest.mark.asyncio

async def test_cancel_subscription(client):
    """Test case for cancel_subscription

    CancelSubscription
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/subscriptions/{subscription_id}/cancel'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_subscription(client):
    """Test case for create_subscription

    CreateSubscription
    """
    body = {"request_body":{"card_id":"ccof:qy5x8hHGYsgLrp4Q4GB","customer_id":"CHFGVKYY8RSV93M5KCYTG4PN0G","idempotency_key":"8193148c-9586-11e6-99f9-28cfe92138cf","location_id":"S8GWD5R9QB376","plan_id":"6JHXF3B2CW3YKHDV4XEM674H","price_override_money":{"amount":100,"currency":"USD"},"start_date":"2020-08-01","tax_percentage":"5","timezone":"America/Los_Angeles"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/subscriptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_subscription_events(client):
    """Test case for list_subscription_events

    ListSubscriptionEvents
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/subscriptions/{subscription_id}/events'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resume_subscription(client):
    """Test case for resume_subscription

    ResumeSubscription
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/subscriptions/{subscription_id}/resume'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_subscription(client):
    """Test case for retrieve_subscription

    RetrieveSubscription
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_subscriptions(client):
    """Test case for search_subscriptions

    SearchSubscriptions
    """
    body = {"request_body":{"query":{"filter":{"customer_ids":["CHFGVKYY8RSV93M5KCYTG4PN0G"],"location_ids":["S8GWD5R9QB376"]}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/subscriptions/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_subscription(client):
    """Test case for update_subscription

    UpdateSubscription
    """
    body = {"request_body":{"subscription":{"price_override_money":{"amount":2000,"currency":"USD"},"tax_percentage":null,"version":1594155459464}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

