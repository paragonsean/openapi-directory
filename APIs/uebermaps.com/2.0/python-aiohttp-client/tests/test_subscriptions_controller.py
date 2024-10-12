# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription import Subscription


pytestmark = pytest.mark.asyncio

async def test_maps_id_subscriptions_delete(client):
    """Test case for maps_id_subscriptions_delete

    Unsubscribe from map
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/maps/{id}/subscriptions'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_subscriptions_get(client):
    """Test case for maps_id_subscriptions_get

    List subscriptions for a given map
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/maps/{id}/subscriptions'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_get(client):
    """Test case for subscriptions_get

    List subscriptions. Pass no parameters to get own subscriptions
    """
    params = [('user_id', 56),
                    ('map_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_post(client):
    """Test case for subscriptions_post

    Create map subscription
    """
    map_id = 3.4
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/subscriptions',
        headers=headers,
        json=map_id,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

