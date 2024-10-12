# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_data_address_interface import CustomerDataAddressInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_v1_customers_customer_id_shipping_address_get(client):
    """Test case for v1_customers_customer_id_shipping_address_get

    customers/{customerId}/shippingAddress
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/customers/{customer_id}/shippingAddress'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

