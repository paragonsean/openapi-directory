# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.pricebycontext_request import PricebycontextRequest
from openapi_server.models.saveprice_request import SavepriceRequest


pytestmark = pytest.mark.asyncio

async def test_deletebysku_id(client):
    """Test case for deletebysku_id

    Delete Price by SKU Id
    """
    params = [('an', '{{accountName}}')]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/price-sheet/{sku_id}'.format(sku_id='sku_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getallpaged(client):
    """Test case for getallpaged

    Get all paged prices
    """
    params = [('an', '{{accountName}}')]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/price-sheet/all/{page}/{page_size}'.format(page='page_example', page_size='page_size_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricebycontext(client):
    """Test case for pricebycontext

    Get Price by context
    """
    body = {"id":6324,"itemId":2390148,"salesChannel":1,"sellerId":"1","validFrom":"1900-01-01T00:00:00","validTo":"4000-01-01T00:00:00"}
    params = [('an', '{{accountName}}')]
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/price-sheet/context',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricebysku_id(client):
    """Test case for pricebysku_id

    Get Price by SKU ID
    """
    params = [('an', '{{accountName}}')]
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/price-sheet/{sku_id}'.format(sku_id='sku_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pricebysku_idandtrade_policy(client):
    """Test case for pricebysku_idandtrade_policy

    Get Price by SKU ID and Trade Policy
    """
    params = [('an', '{{accountName}}')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/price-sheet/{sku_id}/{trade_policy}'.format(sku_id='sku_id_example', trade_policy='trade_policy_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saveprice(client):
    """Test case for saveprice

    Save Price
    """
    body = {"itemId":2390148,"listPrice":1,"price":1,"salesChannel":1,"sellerId":1,"validFrom":"2016-01-01T02:00:00Z","validTo":"2017-01-01T02:00:00Z"}
    params = [('an', '{{accountName}}')]
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/price-sheet',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

