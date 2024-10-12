# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_invoice_order_v1_execute_post_request import SalesInvoiceOrderV1ExecutePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_invoice_order_v1_execute_post(client):
    """Test case for sales_invoice_order_v1_execute_post

    order/{orderId}/invoice
    """
    body = openapi_server.SalesInvoiceOrderV1ExecutePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/order/{order_id}/invoice'.format(order_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

