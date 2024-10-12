# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.single_step_order200_response import SingleStepOrder200Response
from openapi_server.models.single_step_order_request import SingleStepOrderRequest


pytestmark = pytest.mark.asyncio

async def test_single_step_order(client):
    """Test case for single_step_order

    sends an order in a single step.  This is much easier than using other order commands
    """
    body = openapi_server.SingleStepOrderRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/orders/singleStepOrder',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

