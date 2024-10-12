# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.info_result import InfoResult


pytestmark = pytest.mark.asyncio

async def test_get_info(client):
    """Test case for get_info

    Information about versions of application and data.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/sociodemo/sandbox/api/info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

