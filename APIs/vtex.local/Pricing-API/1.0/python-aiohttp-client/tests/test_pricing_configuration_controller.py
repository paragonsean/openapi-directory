# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_pricingv2_status200_response import GetPricingv2Status200Response
from openapi_server.models.pricing_configuration import PricingConfiguration


pytestmark = pytest.mark.asyncio

async def test_get_pricing_config(client):
    """Test case for get_pricing_config

    Get Pricing Configuration
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pricing/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pricingv2_status(client):
    """Test case for get_pricingv2_status

    Get Pricing v2 Status
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pricing/migration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

