# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.save_suggestion_request import SaveSuggestionRequest


pytestmark = pytest.mark.asyncio

async def test_delete_suggestion(client):
    """Test case for delete_suggestion

    Delete SKU Suggestion
    """
    params = [('accountName', 'apiexamples')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/suggestions/{seller_id}/{seller_sku_id}'.format(seller_id='seller123', seller_sku_id='1234'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_suggestion(client):
    """Test case for save_suggestion

    Send SKU Suggestion
    """
    body = {"MeasurementUnit":"MeasurementUnit","SellerStockKeepingUnitId":5,"UnitMultiplier":2,"ProductName":"","Images":[{"imageName":"Principal","imageUrl":"https://i.pinimg.com/originals/2d/96/4a/2d964a6bf37d9224d0615dc85fccdd62.jpg"},{"imageName":"Principal","imageUrl":"https://i.pinimg.com/originals/2d/96/4a/2d964a6bf37d9224d0615dc85fccdd62.jpg"}],"ProductSpecifications":[{"fieldName":"Color","fieldValues":["Red","Green"]},{"fieldName":"Color","fieldValues":["Red","Green"]}],"ProductId":"1234","AvailableQuantity":0,"CategoryFullPath":"CategoryFullPath","Weight":7,"BrandName":"BrandName","EAN":"EAN10","Length":1,"Pricing":{"Currency":"Currency","SalePrice":5,"CurrencySymbol":"CurrencySymbol"},"SellerId":"1","SkuName":"SkuName","Height":6,"ProductDescription":"ProductDescription","SkuSpecifications":[{"fieldName":"color","fieldValues":["Red","Red"]},{"fieldName":"color","fieldValues":["Red","Red"]}],"RefId":"REF10","Width":9}
    params = [('accountName', 'apiexamples')]
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/suggestions/{seller_id}/{seller_sku_id}'.format(seller_id='seller123', seller_sku_id='1234'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

