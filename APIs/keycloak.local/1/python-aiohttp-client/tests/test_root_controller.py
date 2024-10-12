# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.server_info_representation import ServerInfoRepresentation


pytestmark = pytest.mark.asyncio

async def test_root_get(client):
    """Test case for root_get

    Get themes, social providers, auth providers, and event listeners available on this server
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

