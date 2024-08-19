# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.active_subscription_dto import ActiveSubscriptionDTO
from openapi_server.models.subscription_dto import SubscriptionDTO


pytestmark = pytest.mark.asyncio

async def test_are_hooks_supported(client):
    """Test case for are_hooks_supported

    This method can be used to determine if hooks are supported.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/subscription/supports',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all4(client):
    """Test case for get_all4

    Returns all subscriptions
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/subscription',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_subscribe(client):
    """Test case for subscribe

    Subscribe to event
    """
    body = openapi_server.SubscriptionDTO()
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/subscription',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unsubscribe(client):
    """Test case for unsubscribe

    Unsubscribe from event
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/subscription/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

