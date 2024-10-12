# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.baskets import Baskets
from openapi_server.models.config import Config
from openapi_server.models.service_stats import ServiceStats
from openapi_server.models.token import Token


pytestmark = pytest.mark.asyncio

async def test_api_baskets_get(client):
    """Test case for api_baskets_get

    Get baskets
    """
    params = [('max', 56),
                    ('skip', 56),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'service_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/baskets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_baskets_name_delete(client):
    """Test case for api_baskets_name_delete

    Delete basket
    """
    headers = { 
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/baskets/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_baskets_name_get(client):
    """Test case for api_baskets_name_get

    Get basket settings
    """
    headers = { 
        'Accept': 'application/json',
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/baskets/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_baskets_name_post(client):
    """Test case for api_baskets_name_post

    Create new basket
    """
    config = {"expand_path":True,"insecure_tls":False,"forward_url":"https://myservice.example.com/events-collector","proxy_response":False,"capacity":250}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/baskets/{name}'.format(name='name_example'),
        headers=headers,
        json=config,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_baskets_name_put(client):
    """Test case for api_baskets_name_put

    Update basket settings
    """
    config = {"expand_path":True,"insecure_tls":False,"forward_url":"https://myservice.example.com/events-collector","proxy_response":False,"capacity":250}
    headers = { 
        'Content-Type': 'application/json',
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/baskets/{name}'.format(name='name_example'),
        headers=headers,
        json=config,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_stats_get(client):
    """Test case for api_stats_get

    Get baskets statistics
    """
    params = [('max', 56)]
    headers = { 
        'Accept': 'application/json',
        'service_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/stats',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baskets_get(client):
    """Test case for baskets_get

    Get baskets
    """
    params = [('max', 56),
                    ('skip', 56),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'service_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/baskets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baskets_name_delete(client):
    """Test case for baskets_name_delete

    Delete basket
    """
    headers = { 
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/baskets/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baskets_name_get(client):
    """Test case for baskets_name_get

    Get basket settings
    """
    headers = { 
        'Accept': 'application/json',
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/baskets/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baskets_name_post(client):
    """Test case for baskets_name_post

    Create new basket
    """
    config = {"expand_path":True,"insecure_tls":False,"forward_url":"https://myservice.example.com/events-collector","proxy_response":False,"capacity":250}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/baskets/{name}'.format(name='name_example'),
        headers=headers,
        json=config,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_baskets_name_put(client):
    """Test case for baskets_name_put

    Update basket settings
    """
    config = {"expand_path":True,"insecure_tls":False,"forward_url":"https://myservice.example.com/events-collector","proxy_response":False,"capacity":250}
    headers = { 
        'Content-Type': 'application/json',
        'basket_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/baskets/{name}'.format(name='name_example'),
        headers=headers,
        json=config,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

