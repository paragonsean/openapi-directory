# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_amazon_payment_order_information_management_v1_remove_order_reference_delete(client):
    """Test case for amazon_payment_order_information_management_v1_remove_order_reference_delete

    amazon/order-ref
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/amazon/order-ref',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

