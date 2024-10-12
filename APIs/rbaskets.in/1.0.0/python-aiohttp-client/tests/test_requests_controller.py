# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.requests import Requests


pytestmark = pytest.mark.asyncio

async def test_api_baskets_name_requests_delete(client):
    """Test case for api_baskets_name_requests_delete

    Delete all requests
    """
    headers = { 
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/baskets/{name}/requests'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_baskets_name_requests_get(client):
    """Test case for api_baskets_name_requests_get

    Get collected requests
    """
    params = [('max', 56),
                    ('skip', 56),
                    ('q', 'q_example'),
                    ('in', '_in_example')]
    headers = { 
        'Accept': 'application/json',
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/baskets/{name}/requests'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baskets_name_requests_delete(client):
    """Test case for baskets_name_requests_delete

    Delete all requests
    """
    headers = { 
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/baskets/{name}/requests'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baskets_name_requests_get(client):
    """Test case for baskets_name_requests_get

    Get collected requests
    """
    params = [('max', 56),
                    ('skip', 56),
                    ('q', 'q_example'),
                    ('in', '_in_example')]
    headers = { 
        'Accept': 'application/json',
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/baskets/{name}/requests'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

