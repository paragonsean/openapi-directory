# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.shipping_fulfillment import ShippingFulfillment
from openapi_server.models.shipping_fulfillment_details import ShippingFulfillmentDetails
from openapi_server.models.shipping_fulfillment_paged_collection import ShippingFulfillmentPagedCollection


pytestmark = pytest.mark.asyncio

async def test_create_shipping_fulfillment(client):
    """Test case for create_shipping_fulfillment

    
    """
    body = {"lineItems":[{"quantity":0,"lineItemId":"lineItemId"},{"quantity":0,"lineItemId":"lineItemId"}],"shippingCarrierCode":"shippingCarrierCode","shippedDate":"shippedDate","trackingNumber":"trackingNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment'.format(order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shipping_fulfillment(client):
    """Test case for get_shipping_fulfillment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment/{fulfillment_id}'.format(fulfillment_id='fulfillment_id_example', order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shipping_fulfillments(client):
    """Test case for get_shipping_fulfillments

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

