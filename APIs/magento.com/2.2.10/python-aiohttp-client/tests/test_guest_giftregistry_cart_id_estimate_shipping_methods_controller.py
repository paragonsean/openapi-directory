# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.gift_registry_shipping_method_management_v1_estimate_by_registry_id_post_request import GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest
from openapi_server.models.quote_data_shipping_method_interface import QuoteDataShippingMethodInterface


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_gift_registry_guest_cart_shipping_method_management_v1_estimate_by_registry_id_post(client):
    """Test case for gift_registry_guest_cart_shipping_method_management_v1_estimate_by_registry_id_post

    guest-giftregistry/{cartId}/estimate-shipping-methods
    """
    body = openapi_server.GiftRegistryShippingMethodManagementV1EstimateByRegistryIdPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/guest-giftregistry/{cart_id}/estimate-shipping-methods'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

