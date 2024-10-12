# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_domains_add_post(client):
    """Test case for domains_add_post

    Add domain to be managed by SolarVPS Distributed DNS
    """
    params = [('domain', 'domain_example')]
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/domains/add',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_delete_post(client):
    """Test case for domains_delete_post

    Delete domain from SolarVPS Distributed DNS
    """
    params = [('domain', 'domain_example')]
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/domains/delete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_domains_get(client):
    """Test case for domains_get

    View all your domains managed by SolarVPS Distributed DNS
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/domains',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

