# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_customer_account_management_v1_get_confirmation_status_get(client):
    """Test case for customer_account_management_v1_get_confirmation_status_get

    customers/{customerId}/confirm
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/customers/{customer_id}/confirm'.format(customer_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

