# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.license import License


pytestmark = pytest.mark.asyncio

async def test_get_license(client):
    """Test case for get_license

    Get license
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/instance/license',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

