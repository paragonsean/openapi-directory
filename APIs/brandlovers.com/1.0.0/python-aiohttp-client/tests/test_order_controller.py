# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_tracking_refund import NewTrackingRefund
from openapi_server.models.newshipmentstatus import Newshipmentstatus
from openapi_server.models.order import Order


pytestmark = pytest.mark.asyncio

async def test_order_order_id_get(client):
    """Test case for order_order_id_get

    Returns all details of a order
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/marketplace/v1/order/{order_id}'.format(order_id='order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_order_id_shipment_cancel_post(client):
    """Test case for order_order_id_shipment_cancel_post

    Confirm shipment canceletion (when requested by the customer) or failure to deliver
    """
    body = {"number":"number","occurredAt":"2000-01-23T04:56:07.000+00:00","courier":{"taxID":"taxID","name":"name"},"cte":"cte","sellerShipmentId":"sellerShipmentId","tranckingUrl":"tranckingUrl","items":[{"quantity":9,"skuSellerId":"skuSellerId"},{"quantity":9,"skuSellerId":"skuSellerId"}],"info":"info"}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/order/{order_id}/shipment/cancel'.format(order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_order_id_shipment_delivered_post(client):
    """Test case for order_order_id_shipment_delivered_post

    Confirms that a shipment was delivered
    """
    body = {"number":"number","occurredAt":"2000-01-23T04:56:07.000+00:00","courier":{"taxID":"taxID","name":"name"},"cte":"cte","trackingUrl":"trackingUrl","sellerShipmentId":"sellerShipmentId","invoice":{"linkXml":"linkXml","number":"number","accessKey":"accessKey","serie":"serie","cnpj":"cnpj","issuedAt":"2000-01-23T04:56:07.000+00:00","linkDanfe":"linkDanfe"},"items":["items","items"]}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/order/{order_id}/shipment/delivered'.format(order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_order_id_shipment_exchange_post(client):
    """Test case for order_order_id_shipment_exchange_post

    Confirm item exchange
    """
    body = {"number":"number","occurredAt":"2000-01-23T04:56:07.000+00:00","courier":{"taxID":"taxID","name":"name"},"cte":"cte","sellerShipmentId":"sellerShipmentId","tranckingUrl":"tranckingUrl","items":[{"quantity":9,"skuSellerId":"skuSellerId"},{"quantity":9,"skuSellerId":"skuSellerId"}],"info":"info"}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/order/{order_id}/shipment/exchange'.format(order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_order_id_shipment_return_post(client):
    """Test case for order_order_id_shipment_return_post

    Confirm order item return and refund
    """
    body = {"number":"number","occurredAt":"2000-01-23T04:56:07.000+00:00","courier":{"taxID":"taxID","name":"name"},"cte":"cte","sellerShipmentId":"sellerShipmentId","tranckingUrl":"tranckingUrl","items":[{"quantity":9,"skuSellerId":"skuSellerId"},{"quantity":9,"skuSellerId":"skuSellerId"}],"info":"info"}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/order/{order_id}/shipment/return'.format(order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_order_order_id_shipment_sent_post(client):
    """Test case for order_order_id_shipment_sent_post

    Update new order to include shipment information
    """
    body = {"number":"number","occurredAt":"2000-01-23T04:56:07.000+00:00","courier":{"taxID":"taxID","name":"name"},"cte":"cte","trackingUrl":"trackingUrl","sellerShipmentId":"sellerShipmentId","invoice":{"linkXml":"linkXml","number":"number","accessKey":"accessKey","serie":"serie","cnpj":"cnpj","issuedAt":"2000-01-23T04:56:07.000+00:00","linkDanfe":"linkDanfe"},"items":["items","items"]}
    headers = { 
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/marketplace/v1/order/{order_id}/shipment/sent'.format(order_id='order_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

