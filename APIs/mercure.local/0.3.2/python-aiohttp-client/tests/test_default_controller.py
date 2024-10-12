# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscriptions import Subscriptions


pytestmark = pytest.mark.asyncio

async def test_well_known_mercure_get(client):
    """Test case for well_known_mercure_get

    Subscribe to updates
    """
    params = [('topic', ['topic_example']),
                    ('Last-Event-ID', 'last_event_id_example')]
    headers = { 
        'Accept': 'text/event-stream',
        'last_event_id2': 'last_event_id_example',
        'Cookie': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/.well-known/mercure',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_well_known_mercure_post(client):
    """Test case for well_known_mercure_post

    Publish an update
    """
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'data': 'data_example',
        'id': 'id_example',
        'private': True,
        'retry': 56,
        'topic': ['topic_example'],
        'type': 'type_example'
        }
    response = await client.request(
        method='POST',
        path='/.well-known/mercure',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_well_known_mercure_subscriptions_get(client):
    """Test case for well_known_mercure_subscriptions_get

    Active subscriptions
    """
    headers = { 
        'Accept': 'application/ld+json',
        'Cookie': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/.well-known/mercure/subscriptions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_well_known_mercure_subscriptions_topic_get(client):
    """Test case for well_known_mercure_subscriptions_topic_get

    Active subscriptions for the given topic
    """
    headers = { 
        'Accept': 'application/ld+json',
        'Cookie': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/.well-known/mercure/subscriptions/{topic}'.format(topic='topic_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_well_known_mercure_subscriptions_topic_subscriber_get(client):
    """Test case for well_known_mercure_subscriptions_topic_subscriber_get

    Active subscription for the given topic and subscriber
    """
    headers = { 
        'Accept': 'application/ld+json',
        'Cookie': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/.well-known/mercure/subscriptions/{topic}/{subscriber}'.format(topic='topic_example', subscriber='subscriber_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

