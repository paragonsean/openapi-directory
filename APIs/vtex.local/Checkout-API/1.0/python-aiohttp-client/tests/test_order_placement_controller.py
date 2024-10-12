# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.place_order200_response import PlaceOrder200Response
from openapi_server.models.place_order_from_existing_order_form_request import PlaceOrderFromExistingOrderFormRequest
from openapi_server.models.place_order_request import PlaceOrderRequest
from openapi_server.models.process_order500_response import ProcessOrder500Response


pytestmark = pytest.mark.asyncio

async def test_place_order(client):
    """Test case for place_order

    Place order
    """
    body = openapi_server.PlaceOrderRequest()
    params = [('sc', 1)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/checkout/pub/orders',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_order_from_existing_order_form(client):
    """Test case for place_order_from_existing_order_form

    Place order from an existing cart
    """
    body = openapi_server.PlaceOrderFromExistingOrderFormRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/orderForm/{order_form_id}/transaction'.format(order_form_id='ede846222cd44046ba6c638442c3505a'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_process_order(client):
    """Test case for process_order

    Process order
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'cookie': 'Vtex_CHKO_Auth=0e/RpYIEZu19BuwXB4tZ7eIGu9HT8vdUAHWQDHDpxMc=; CheckoutDataAccess=0e/PoiTEZu19BuwXB4tZ7eIGu9HT8vdUAHWQDHDpxMc=',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pub/gatewayCallback/{order_group}'.format(order_group='123456789'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

