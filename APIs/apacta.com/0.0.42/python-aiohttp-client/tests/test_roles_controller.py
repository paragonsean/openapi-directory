# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.roles_get200_response import RolesGet200Response


pytestmark = pytest.mark.asyncio

async def test_roles_get(client):
    """Test case for roles_get

    Get a list of roles
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/roles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

