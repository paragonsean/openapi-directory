# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_order2200_response import CancelOrder2200Response
from openapi_server.models.invoice_notification_request import InvoiceNotificationRequest


pytestmark = pytest.mark.asyncio

async def test_invoice_notification2(client):
    """Test case for invoice_notification2

    Order invoice notification
    """
    body = {"courier":null,"extraValue":100,"invoiceKey":null,"invoiceNumber":"9999","invoiceUrl":null,"invoiceValue":2499,"issuedDate":"2019-01-30","items":[{"id":"1234","price":10000,"quantity":1}],"trackingNumber":null,"trackingUrl":null,"type":"Output"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/orders/pvt/document/{order_id}/invoices'.format(order_id='70caf3941s6df1'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

