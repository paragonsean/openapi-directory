# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_collection import ActionCollection
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_permissions(client):
    """Test case for get_permissions

    List permissions
    """
    params = [('limit', 100),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/permissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

