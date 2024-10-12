# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_user_in_group_request import CreateUserInGroupRequest


pytestmark = pytest.mark.asyncio

async def test_create_user_in_group(client):
    """Test case for create_user_in_group

    Create User in Group
    """
    body = {"groupIds":["{{groupId}}"],"profile":{"email":"isaac@{{email-suffix}}","firstName":"Isaac","lastName":"Brock","login":"isaac@{{email-suffix}}"}}
    params = [('activate', 'false')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

