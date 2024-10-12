# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_billing_address_management_v1_assign_post_request import QuoteBillingAddressManagementV1AssignPostRequest
from openapi_server.models.quote_data_address_interface import QuoteDataAddressInterface


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_quote_guest_billing_address_management_v1_assign_post(client):
    """Test case for quote_guest_billing_address_management_v1_assign_post

    guest-carts/{cartId}/billing-address
    """
    body = openapi_server.QuoteBillingAddressManagementV1AssignPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/guest-carts/{cart_id}/billing-address'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quote_guest_billing_address_management_v1_get_get(client):
    """Test case for quote_guest_billing_address_management_v1_get_get

    guest-carts/{cartId}/billing-address
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/guest-carts/{cart_id}/billing-address'.format(cart_id='cart_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

