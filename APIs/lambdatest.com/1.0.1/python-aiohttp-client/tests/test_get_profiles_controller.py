# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.profiles import Profiles


pytestmark = pytest.mark.asyncio

async def test_profiles(client):
    """Test case for profiles

    Fetch login profiles
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/screenshots/v1/profiles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

