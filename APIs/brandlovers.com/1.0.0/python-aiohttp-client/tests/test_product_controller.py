# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_product import GetProduct
from openapi_server.models.product import Product
from openapi_server.models.product_price import ProductPrice
from openapi_server.models.seller_item_status import SellerItemStatus
from openapi_server.models.stock import Stock


pytestmark = pytest.mark.asyncio

async def test_product_post(client):
    """Test case for product_post

    Create a new product to the marketplace
    """
    product = {"gtin":["gtin","gtin"],"images":["images","images"],"productId":"productId","productGroupId":"productGroupId","description":"description","videos":["videos","videos"],"title":"title","skuSellerId":"skuSellerId","price":{"offer":7,"default":2},"attributes":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"categories":["categories","categories"],"giftWrap":{"messageSupport":True,"available":True,"value":5},"stock":9,"brand":"brand","dimensions":{"length":6,"width":5,"weight":1,"height":0}}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/product',
        headers=headers,
        json=product,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_sku_seller_id_get(client):
    """Test case for product_sku_seller_id_get

    Returns details of a single product using the seller `skuSellerId`
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/product/{sku_seller_id}'.format(sku_seller_id='sku_seller_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_sku_seller_id_prices_put(client):
    """Test case for product_sku_seller_id_prices_put

    Allows seller to update prices of a single SKU
    """
    body = {"offer":7,"default":2}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/marketplace/v1/product/{sku_seller_id}/prices'.format(sku_seller_id='sku_seller_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_sku_seller_id_status_put(client):
    """Test case for product_sku_seller_id_status_put

    Enable/disable a single product in the Marketplace
    """
    body = {"active":True}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/marketplace/v1/product/{sku_seller_id}/status'.format(sku_seller_id='sku_seller_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_product_sku_seller_id_stock_put(client):
    """Test case for product_sku_seller_id_stock_put

    Update a single product stock
    """
    body = {"quantity":6,"crossDockingTime":0}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/marketplace/v1/product/{sku_seller_id}/stock'.format(sku_seller_id='sku_seller_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

