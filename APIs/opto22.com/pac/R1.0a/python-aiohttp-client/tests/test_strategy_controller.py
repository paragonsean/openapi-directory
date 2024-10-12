# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response400_bad_admin_or_value import ErrorResponse400BadAdminOrValue
from openapi_server.models.error_response401_bad_key_for_basic_auth import ErrorResponse401BadKeyForBasicAuth
from openapi_server.models.strategy_response import StrategyResponse


pytestmark = pytest.mark.asyncio

async def test_read_strategy_details_0(client):
    """Test case for read_strategy_details_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/device/strategy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

