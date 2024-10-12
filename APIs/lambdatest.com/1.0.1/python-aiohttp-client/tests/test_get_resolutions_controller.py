# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_denied import AccessDenied
from openapi_server.models.resolutions import Resolutions


pytestmark = pytest.mark.asyncio

async def test_resolutions(client):
    """Test case for resolutions

    Fetch all available resolution on different OS
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/screenshots/v1/resolutions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

