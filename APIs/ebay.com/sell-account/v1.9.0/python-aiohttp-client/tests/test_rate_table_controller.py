# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rate_table_response import RateTableResponse


pytestmark = pytest.mark.asyncio

async def test_get_rate_tables(client):
    """Test case for get_rate_tables

    
    """
    params = [('country_code', 'country_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/account/v1/rate_table',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

