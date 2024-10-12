# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.confirm_order_body import ConfirmOrderBody
from openapi_server.models.create_order_body import CreateOrderBody
from openapi_server.models.order import Order
from openapi_server.models.order_confirm_post200_response import OrderConfirmPost200Response
from openapi_server.models.order_create_post200_response import OrderCreatePost200Response
from openapi_server.models.order_shipping_post200_response import OrderShippingPost200Response
from openapi_server.models.shipping_options_body import ShippingOptionsBody


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_order_confirm_post(client):
    """Test case for order_confirm_post

    Confirms an order from a quote_id and submits it to the Voodoo factory. 
    """
    body = openapi_server.ConfirmOrderBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/2/order/confirm',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_order_create_post(client):
    """Test case for order_create_post

    Quotes an order and returns a quote_id that is used to confirm the order. 
    """
    body = openapi_server.CreateOrderBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/2/order/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_get(client):
    """Test case for order_get

    Lists all orders. 
    """
    headers = { 
        'Accept': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/2/order',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_order_id_get(client):
    """Test case for order_order_id_get

    Retrieve a previously created model by its id. 
    """
    headers = { 
        'Accept': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/2/order/{order_id}'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_order_shipping_post(client):
    """Test case for order_shipping_post

    List shipping options and prices for a given shipment. 
    """
    body = openapi_server.ShippingOptionsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Voodoo Manufacturing API Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/2/order/shipping',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

