# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.body import Body
from openapi_server.models.body1 import Body1
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.personalised_categories_response import PersonalisedCategoriesResponse


pytestmark = pytest.mark.asyncio

async def test_my_categories_follows_delete(client):
    """Test case for my_categories_follows_delete

    Unfollow category
    """
    body = openapi_server.Body1()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/my/categories/follows',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_categories_follows_get(client):
    """Test case for my_categories_follows_get

    List of followed categories
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
        path='/my/categories/follows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_my_categories_follows_post(client):
    """Test case for my_categories_follows_post

    Follow category
    """
    body = {"category_id":"category_id","platform":"responsiveweb"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/categories/follows',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

