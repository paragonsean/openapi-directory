# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_payment_interface import QuoteDataPaymentInterface
from openapi_server.models.quote_payment_method_management_v1_set_put_request import QuotePaymentMethodManagementV1SetPutRequest


pytestmark = pytest.mark.asyncio

async def test_quote_guest_payment_method_management_v1_get_get(client):
    """Test case for quote_guest_payment_method_management_v1_get_get

    guest-carts/{cartId}/selected-payment-method
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/guest-carts/{cart_id}/selected-payment-method'.format(cart_id='cart_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_quote_guest_payment_method_management_v1_set_put(client):
    """Test case for quote_guest_payment_method_management_v1_set_put

    guest-carts/{cartId}/selected-payment-method
    """
    body = openapi_server.QuotePaymentMethodManagementV1SetPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/guest-carts/{cart_id}/selected-payment-method'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

