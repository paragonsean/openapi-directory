# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model400 import Model400
from openapi_server.models.model404 import Model404
from openapi_server.models.post_compile200_response import PostCompile200Response


pytestmark = pytest.mark.asyncio

async def test_get_query(client):
    """Test case for get_query

    Execute an ad-hoc query (simple)
    """
    params = [('q', '{\"query\": \"data.servers[i].ports[_] = \\\"p2\\\"; data.servers[i].name = name\"}'),
                    ('pretty', true),
                    ('explain', 'full'),
                    ('metrics', false)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/query',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-yaml not supported by Connexion")
async def test_post_query(client):
    """Test case for post_query

    Execute an ad-hoc query (complex)
    """
    body = None
    params = [('pretty', true),
                    ('explain', 'full'),
                    ('metrics', false)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-yaml',
    }
    response = await client.request(
        method='POST',
        path='/v1/query',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_simple_query(client):
    """Test case for post_simple_query

    Execute a simple query
    """
    body = None
    params = [('pretty', true)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

