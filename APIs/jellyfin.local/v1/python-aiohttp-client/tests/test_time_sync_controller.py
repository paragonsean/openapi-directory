# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.utc_time_response import UtcTimeResponse


pytestmark = pytest.mark.asyncio

async def test_get_utc_time(client):
    """Test case for get_utc_time

    Gets the current UTC time.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/GetUtcTime',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

