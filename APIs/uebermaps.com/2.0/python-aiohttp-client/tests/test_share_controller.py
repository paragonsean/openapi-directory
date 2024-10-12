# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.map_with_auth_token import MapWithAuthToken


pytestmark = pytest.mark.asyncio

async def test_share_map_id_get(client):
    """Test case for share_map_id_get

    Get secret access token to share map
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/share/map/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

