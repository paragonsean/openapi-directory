# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.profile import Profile


pytestmark = pytest.mark.asyncio

async def test_profile_get(client):
    """Test case for profile_get

    Get profile
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/profile',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

