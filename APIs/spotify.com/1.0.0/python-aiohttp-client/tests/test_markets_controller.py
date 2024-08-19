# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_available_markets200_response import GetAvailableMarkets200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response


pytestmark = pytest.mark.asyncio

async def test_get_available_markets(client):
    """Test case for get_available_markets

    Get Available Markets 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/markets',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

