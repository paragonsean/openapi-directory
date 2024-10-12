# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.basket_info200_response import BasketInfo200Response
from openapi_server.models.basket_item_add200_response import BasketItemAdd200Response
from openapi_server.models.basket_live_shipping_service_create200_response import BasketLiveShippingServiceCreate200Response
from openapi_server.models.basket_live_shipping_service_delete200_response import BasketLiveShippingServiceDelete200Response
from openapi_server.models.basket_live_shipping_service_list200_response import BasketLiveShippingServiceList200Response


pytestmark = pytest.mark.asyncio

async def test_basket_info(client):
    """Test case for basket_info

    
    """
    params = [('id', 'id_example'),
                    ('store_id', 'store_id_example'),
                    ('params', 'force_all'),
                    ('exclude', 'exclude_example'),
                    ('response_fields', 'response_fields_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/basket.info.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_basket_item_add(client):
    """Test case for basket_item_add

    
    """
    params = [('customer_id', 'customer_id_example'),
                    ('product_id', 'product_id_example'),
                    ('variant_id', 'variant_id_example'),
                    ('quantity', 0),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/basket.item.add.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_basket_live_shipping_service_create(client):
    """Test case for basket_live_shipping_service_create

    
    """
    params = [('store_id', 'store_id_example'),
                    ('name', 'name_example'),
                    ('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/basket.live_shipping_service.create.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_basket_live_shipping_service_delete(client):
    """Test case for basket_live_shipping_service_delete

    
    """
    params = [('id', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/basket.live_shipping_service.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_basket_live_shipping_service_list(client):
    """Test case for basket_live_shipping_service_list

    
    """
    params = [('store_id', 'store_id_example'),
                    ('start', 0),
                    ('count', 10)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/basket.live_shipping_service.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

