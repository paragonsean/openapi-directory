# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_user import JsonUser


pytestmark = pytest.mark.asyncio

async def test_resource10_user_user_id_get_user_get(client):
    """Test case for resource10_user_user_id_get_user_get

    Get a user by userId.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/1.0/user/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

