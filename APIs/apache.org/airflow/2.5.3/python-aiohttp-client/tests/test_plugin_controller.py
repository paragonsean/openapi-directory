# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.plugin_collection import PluginCollection


pytestmark = pytest.mark.asyncio

async def test_get_plugins(client):
    """Test case for get_plugins

    Get a list of loaded plugins
    """
    params = [('limit', 100),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/plugins',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

