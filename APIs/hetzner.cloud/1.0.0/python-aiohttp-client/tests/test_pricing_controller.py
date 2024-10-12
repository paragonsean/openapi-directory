# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pricing_get200_response import PricingGet200Response


pytestmark = pytest.mark.asyncio

async def test_pricing_get(client):
    """Test case for pricing_get

    Get all prices
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/pricing',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

