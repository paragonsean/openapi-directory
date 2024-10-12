# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_management_v1_assign_customer_put_request import QuoteCartManagementV1AssignCustomerPutRequest
from openapi_server.models.quote_data_cart_interface import QuoteDataCartInterface


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_quote_guest_cart_management_v1_assign_customer_put(client):
    """Test case for quote_guest_cart_management_v1_assign_customer_put

    guest-carts/{cartId}
    """
    body = openapi_server.QuoteCartManagementV1AssignCustomerPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/guest-carts/{cart_id}'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_guest_cart_repository_v1_get_get(client):
    """Test case for quote_guest_cart_repository_v1_get_get

    guest-carts/{cartId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/guest-carts/{cart_id}'.format(cart_id='cart_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

