# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.me_model import MeModel


pytestmark = pytest.mark.asyncio

async def test_get_me(client):
    """Test case for get_me

    Get authenticated user details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

