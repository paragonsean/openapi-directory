# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_usage_list import ApiUsageList


pytestmark = pytest.mark.asyncio

async def test_get_api_usage_plans_v2(client):
    """Test case for get_api_usage_plans_v2

    Get API Isage
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/apiusage',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

