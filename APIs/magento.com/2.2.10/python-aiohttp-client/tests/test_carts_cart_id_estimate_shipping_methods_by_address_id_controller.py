# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_shipping_method_interface import QuoteDataShippingMethodInterface
from openapi_server.models.quote_shipping_method_management_v1_estimate_by_address_id_post_request import QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_carts_cart_id_estimate_shipping_methods_by_address_id_post(client):
    """Test case for v1_carts_cart_id_estimate_shipping_methods_by_address_id_post

    carts/{cartId}/estimate-shipping-methods-by-address-id
    """
    body = openapi_server.QuoteShippingMethodManagementV1EstimateByAddressIdPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/carts/{cart_id}/estimate-shipping-methods-by-address-id'.format(cart_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

