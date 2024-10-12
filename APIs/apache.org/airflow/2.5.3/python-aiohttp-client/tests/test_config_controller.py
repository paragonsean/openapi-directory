# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config import Config
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_config(client):
    """Test case for get_config

    Get current configuration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

