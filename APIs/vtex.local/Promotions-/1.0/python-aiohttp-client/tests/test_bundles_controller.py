# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calculatediscountsandtaxes_bundles_request import CalculatediscountsandtaxesBundlesRequest


pytestmark = pytest.mark.asyncio

async def test_calculatediscountsandtaxes_bundles(client):
    """Test case for calculatediscountsandtaxes_bundles

    Calculate discounts and taxes (Bundles)
    """
    body = {"isShoppingCart":true,"items":[{"id":"160","index":0,"isGift":false,"logisticsInfos":[],"measurementUnit":"un","params":[{"name":"Seller@CatalogSystem","value":"1"},{"name":"product@CatalogSystem","value":"94"}],"priceSheet":[],"priceTags":[],"productSpecifications":[],"quantity":3,"sellerId":"1","unitMultiplier":1}],"origin":"Marketplace","params":[{"name":"product@CatalogSystem","value":"2662"},{"name":"couponCode@Marketing","value":"coupon"}],"profileId":"aa","salesChannel":"1"}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pub/bundles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

