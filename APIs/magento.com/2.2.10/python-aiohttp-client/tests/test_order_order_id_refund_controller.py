# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_refund_order_v1_execute_post_request import SalesRefundOrderV1ExecutePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_refund_order_v1_execute_post(client):
    """Test case for sales_refund_order_v1_execute_post

    order/{orderId}/refund
    """
    body = openapi_server.SalesRefundOrderV1ExecutePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/order/{order_id}/refund'.format(order_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

