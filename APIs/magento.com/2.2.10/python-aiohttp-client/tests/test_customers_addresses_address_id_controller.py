# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_data_address_interface import CustomerDataAddressInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_customer_address_repository_v1_get_by_id_get(client):
    """Test case for customer_address_repository_v1_get_by_id_get

    customers/addresses/{addressId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/customers/addresses/{address_id}'.format(address_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

