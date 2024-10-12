# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_interference(client):
    """Test case for interference

    Find the best server for overlapping coverage
    """
    params = [('network', 'network_example'),
                    ('name', 'name_example')]
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/interference',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mesh(client):
    """Test case for mesh

    Merge sites into a super layer.
    """
    params = [('network', 'network_example'),
                    ('name', 'name_example')]
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/mesh',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network(client):
    """Test case for network

    Find the best server for somewhere
    """
    params = [('net', 'net_example'),
                    ('nam', 'nam_example'),
                    ('lat', 3.4),
                    ('lon', 3.4),
                    ('alt', 56),
                    ('rxg', 3.4)]
    headers = { 
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/network',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

