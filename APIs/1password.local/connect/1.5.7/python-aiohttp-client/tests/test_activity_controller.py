# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_request import APIRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_get_api_activity(client):
    """Test case for get_api_activity

    Retrieve a list of API Requests that have been made.
    """
    params = [('limit', 50),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/activity',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

