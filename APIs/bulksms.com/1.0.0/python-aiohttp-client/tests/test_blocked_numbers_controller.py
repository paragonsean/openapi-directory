# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.blocked_number import BlockedNumber


pytestmark = pytest.mark.asyncio

async def test_blocked_numbers_get(client):
    """Test case for blocked_numbers_get

    List blocked numbers
    """
    params = [('min-id', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/blocked-numbers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blocked_numbers_post(client):
    """Test case for blocked_numbers_post

    Create a blocked number
    """
    body = ['body_example']
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v1/blocked-numbers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

