# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.system_status_response_schema import SystemStatusResponseSchema


pytestmark = pytest.mark.asyncio

async def test_systemstatus_get(client):
    """Test case for systemstatus_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/mdes/csapi/v2/systemstatus',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

