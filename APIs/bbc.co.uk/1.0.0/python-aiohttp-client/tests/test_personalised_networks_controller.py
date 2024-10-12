# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.body2 import Body2
from openapi_server.models.body3 import Body3
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.personalised_networks_response import PersonalisedNetworksResponse


pytestmark = pytest.mark.asyncio

async def test_my_networks_follows_delete(client):
    """Test case for my_networks_follows_delete

    Unfollow network
    """
    body = openapi_server.Body3()
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/my/networks/follows',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_networks_follows_get(client):
    """Test case for my_networks_follows_get

    List of followed networks
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/networks/follows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_networks_follows_post(client):
    """Test case for my_networks_follows_post

    Follow network
    """
    body = openapi_server.Body2()
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/networks/follows',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

