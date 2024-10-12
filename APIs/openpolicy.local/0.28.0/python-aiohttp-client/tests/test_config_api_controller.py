# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model200_single_result import Model200SingleResult
from openapi_server.models.model400 import Model400


pytestmark = pytest.mark.asyncio

async def test_get_config(client):
    """Test case for get_config

    Get configurations
    """
    params = [('pretty', true)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/config',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

