# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_order200_response import CancelOrder200Response
from openapi_server.models.invoice_notification_request import InvoiceNotificationRequest
from openapi_server.models.updatepartialinvoice_send_tracking_number import UpdatepartialinvoiceSendTrackingNumber
from openapi_server.models.updatepartialinvoice_send_tracking_number_request import UpdatepartialinvoiceSendTrackingNumberRequest


pytestmark = pytest.mark.asyncio

async def test_invoice_notification(client):
    """Test case for invoice_notification

    Order invoice notification
    """
    body = {"courier":null,"dispatchedDate":"2019-01-31T18:25:43-05:00","invoiceKey":null,"invoiceNumber":"9999","invoiceUrl":null,"invoiceValue":"10000","issuanceDate":"2019-01-302019-01-31T18:25:43-05:00","items":[{"id":"1234","price":10000,"quantity":1}],"trackingNumber":null,"trackingUrl":null,"type":"Output"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/oms/pvt/orders/{order_id}/invoice'.format(order_id='1172452900788-01'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_updatepartialinvoice_send_tracking_number(client):
    """Test case for updatepartialinvoice_send_tracking_number

    Update order's partial invoice (send tracking number)
    """
    body = {"courier":"carrierOne","dispatchedDate":"2022-02-08T13:16:13.4617653+00:00","trackingNumber":"87658","trackingUrl":"https://www.tracking.com/url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/oms/pvt/orders/{order_id}/invoice/{invoice_number}'.format(order_id='1172452900788-01', invoice_number='000030711'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

