# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.networks_response import NetworksResponse
from openapi_server.models.radio_error_response import RadioErrorResponse


pytestmark = pytest.mark.asyncio

async def test_get_radio_networks(client):
    """Test case for get_radio_networks

    Networks
    """
    params = [('preset', True),
                    ('international', True)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/radio/networks.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

