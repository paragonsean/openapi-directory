# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_pods_get(client):
    """Test case for pods_get

    View all your pods
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pods',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pods_pod_id_action_get(client):
    """Test case for pods_pod_id_action_get

    Perform action on a specific pod
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pods/{pod_id}/{action}'.format(pod_id=3.4, action='action_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pods_pod_id_get(client):
    """Test case for pods_pod_id_get

    View information on a specific pod
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pods/{pod_id}'.format(pod_id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pods_pod_id_ping_get(client):
    """Test case for pods_pod_id_ping_get

    Ping your specified pod
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pods/{pod_id}/ping'.format(pod_id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

