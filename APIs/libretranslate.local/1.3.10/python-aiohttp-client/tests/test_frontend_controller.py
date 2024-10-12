# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.frontend_settings import FrontendSettings


pytestmark = pytest.mark.asyncio

async def test_frontend_settings_get(client):
    """Test case for frontend_settings_get

    Retrieve frontend specific settings
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/frontend/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

