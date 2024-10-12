# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credits_response import CreditsResponse
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_credits_balance_get(client):
    """Test case for credits_balance_get

    
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/credits/balance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

