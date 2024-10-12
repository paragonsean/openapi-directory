# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.server_information import ServerInformation


pytestmark = pytest.mark.asyncio

async def test_get_server_info(client):
    """Test case for get_server_info

    Get Jira instance info
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/serverInfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

