# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.checkout_data_payment_details_interface import CheckoutDataPaymentDetailsInterface
from openapi_server.models.checkout_shipping_information_management_v1_save_address_information_post_request import CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_checkout_shipping_information_management_v1_save_address_information_post(client):
    """Test case for checkout_shipping_information_management_v1_save_address_information_post

    carts/mine/shipping-information
    """
    body = openapi_server.CheckoutShippingInformationManagementV1SaveAddressInformationPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/carts/mine/shipping-information',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

