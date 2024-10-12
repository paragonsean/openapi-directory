# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_users_id_get(client):
    """Test case for users_id_get

    Get user profile
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

