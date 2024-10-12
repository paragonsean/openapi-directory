# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.events_v1_subscription_subscribed_event import EventsV1SubscriptionSubscribedEvent
from openapi_server.models.list_subscribed_event_response import ListSubscribedEventResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_subscribed_event(client):
    """Test case for create_subscribed_event

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'schema_version': 56,
        'type': 'type_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Subscriptions/{subscription_sid}/SubscribedEvents'.format(subscription_sid='subscription_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_subscribed_event(client):
    """Test case for delete_subscribed_event

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}'.format(subscription_sid='subscription_sid_example', type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_subscribed_event(client):
    """Test case for fetch_subscribed_event

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}'.format(subscription_sid='subscription_sid_example', type='type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_subscribed_event(client):
    """Test case for list_subscribed_event

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Subscriptions/{subscription_sid}/SubscribedEvents'.format(subscription_sid='subscription_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_subscribed_event(client):
    """Test case for update_subscribed_event

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'schema_version': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Subscriptions/{subscription_sid}/SubscribedEvents/{type}'.format(subscription_sid='subscription_sid_example', type='type_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

