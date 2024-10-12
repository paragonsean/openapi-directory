# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_products_response import GetProductsResponse
from openapi_server.models.get_products_status_selling import GetProductsStatusSelling
from openapi_server.models.get_seller_products_status import GetSellerProductsStatus
from openapi_server.models.product import Product
from openapi_server.models.product_status_update import ProductStatusUpdate
from openapi_server.models.product_stock import ProductStock
from openapi_server.models.product_update import ProductUpdate
from openapi_server.models.seller_item_prices import SellerItemPrices


pytestmark = pytest.mark.asyncio

async def test_product_sku_seller_id_put(client):
    """Test case for product_sku_seller_id_put

    Update product details
    """
    body = {"gtin":["gtin","gtin"],"images":["images","images"],"productId":"productId","productGroupId":"productGroupId","description":"description","videos":["videos","videos"],"title":"title","skuSellerId":"skuSellerId","price":{"offer":7,"default":2},"attributes":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"categories":["categories","categories"],"giftWrap":{"messageSupport":True,"available":True,"value":5},"stock":0,"brand":"brand","dimensions":{"length":6,"width":5,"weight":1,"height":0}}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/marketplace/v1/product/{sku_seller_id}'.format(sku_seller_id='sku_seller_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_get(client):
    """Test case for products_get

    Returns a list of products loaded into BrandLovers Marketplace
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
        'authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/products',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_post(client):
    """Test case for products_post

    Allows new products from the seller to be loaded into the marketplace
    """
    products = {"gtin":["gtin","gtin"],"images":["images","images"],"productId":"productId","productGroupId":"productGroupId","description":"description","videos":["videos","videos"],"title":"title","skuSellerId":"skuSellerId","price":{"offer":7,"default":2},"attributes":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"categories":["categories","categories"],"giftWrap":{"messageSupport":True,"available":True,"value":5},"stock":9,"brand":"brand","dimensions":{"length":6,"width":5,"weight":1,"height":0}}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/products',
        headers=headers,
        json=products,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_prices_put(client):
    """Test case for products_prices_put

    Allows bulk update of product prices.
    """
    body = {"price":{"offer":7,"default":2},"skuSellerId":"skuSellerId"}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/marketplace/v1/products/prices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_status_get(client):
    """Test case for products_status_get

    Returns seller products status in the marketplace
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/products/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_status_put(client):
    """Test case for products_status_put

    Bulk enable/disable products in the marketplace
    """
    body = {"active":True,"skuSellerId":"skuSellerId"}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/marketplace/v1/products/status',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_status_selling_get(client):
    """Test case for products_status_selling_get

    Returns products that are successfully listed for sale.
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/products/status/selling',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_products_stocks_put(client):
    """Test case for products_stocks_put

    Bulk product stock update
    """
    body = {"skuSellerId":"skuSellerId","stocks":[{"quantity":6,"crossDockingTime":0},{"quantity":6,"crossDockingTime":0}]}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/marketplace/v1/products/stocks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

