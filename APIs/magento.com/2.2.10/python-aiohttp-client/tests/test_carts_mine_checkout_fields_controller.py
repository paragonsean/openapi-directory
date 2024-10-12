# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_quote_cart_checkout_field_management_v1_save_checkout_fields_post_request import TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_temando_shipping_quote_cart_checkout_field_management_v1_save_checkout_fields_post(client):
    """Test case for temando_shipping_quote_cart_checkout_field_management_v1_save_checkout_fields_post

    carts/mine/checkout-fields
    """
    body = openapi_server.TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/carts/mine/checkout-fields',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

