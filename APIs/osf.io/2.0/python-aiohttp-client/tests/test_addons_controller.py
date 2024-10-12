# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addon import Addon


pytestmark = pytest.mark.asyncio

async def test_addons_list(client):
    """Test case for addons_list

    List all addons
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/addons/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

