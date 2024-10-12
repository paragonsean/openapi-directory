# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_users200_response import GetUsers200Response


pytestmark = pytest.mark.asyncio

async def test_get_users(client):
    """Test case for get_users

    List Users
    """
    params = [('page_size', 10),
                    ('order', asc),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v0.2/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

