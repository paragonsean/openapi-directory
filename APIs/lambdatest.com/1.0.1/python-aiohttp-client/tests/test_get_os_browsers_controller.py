# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.os_browsers import OsBrowsers


pytestmark = pytest.mark.asyncio

async def test_os_browsers(client):
    """Test case for os_browsers

    Fetch all available os-browser combinations.
    """
    params = [('os', 'os_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/screenshots/v1/os-browsers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

