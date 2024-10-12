# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_cart_management_v1_place_order_put_request import QuoteCartManagementV1PlaceOrderPutRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_quote_guest_cart_management_v1_place_order_put(client):
    """Test case for quote_guest_cart_management_v1_place_order_put

    guest-carts/{cartId}/order
    """
    body = openapi_server.QuoteCartManagementV1PlaceOrderPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/guest-carts/{cart_id}/order'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

