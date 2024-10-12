# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config_external_price_source_request import ConfigExternalPriceSourceRequest
from openapi_server.models.get_prices_request_object import GetPricesRequestObject
from openapi_server.models.response2 import Response2


pytestmark = pytest.mark.asyncio

async def test_api_pricing_hub_prices_post(client):
    """Test case for api_pricing_hub_prices_post

    Get Prices
    """
    body = {"UtmCampaign":"summer","UtmInternalCampaign":"sale","UtmMedium":"social","UtmSource":"facebook","email":"customer@email.com","items":[{"brandId":"2000000","categoriesIds":["1"],"index":0,"priceTableIds":[],"quantity":1,"sellerId":"1","skuId":"13"}],"salesChannel":"1"}
    params = [('accountName', 'apiexamples')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/pricing-hub/prices',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_config_external_price_source(client):
    """Test case for config_external_price_source

    Configure External Price Source
    """
    body = {"active":True,"appName":"apiexamples_app_name"}
    params = [('an', 'apiexamples')]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'x_vtex_api_app_key': '{{X-VTEX-API-AppKey}}',
        'x_vtex_api_app_token': '{{X-VTEX-API-AppToken}}',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/config',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

