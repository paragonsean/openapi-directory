# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.spec import Spec


pytestmark = pytest.mark.asyncio

async def test_specs(client):
    """Test case for specs

    Fetch Swagger information
    """
    headers = { 
        'Accept': 'application/json',
        'wsc-api-key': 'special-key',
        'wsc-access-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/api/v1/specs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

