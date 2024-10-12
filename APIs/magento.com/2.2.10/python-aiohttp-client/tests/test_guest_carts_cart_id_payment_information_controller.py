# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.checkout_data_payment_details_interface import CheckoutDataPaymentDetailsInterface
from openapi_server.models.checkout_guest_payment_information_management_v1_save_payment_information_and_place_order_post_request import CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_checkout_guest_payment_information_management_v1_get_payment_information_get(client):
    """Test case for checkout_guest_payment_information_management_v1_get_payment_information_get

    guest-carts/{cartId}/payment-information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/guest-carts/{cart_id}/payment-information'.format(cart_id='cart_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_checkout_guest_payment_information_management_v1_save_payment_information_and_place_order_post(client):
    """Test case for checkout_guest_payment_information_management_v1_save_payment_information_and_place_order_post

    guest-carts/{cartId}/payment-information
    """
    body = openapi_server.CheckoutGuestPaymentInformationManagementV1SavePaymentInformationAndPlaceOrderPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/guest-carts/{cart_id}/payment-information'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

