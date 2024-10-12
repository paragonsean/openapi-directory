# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.amazon_payment_address_management_v1_get_billing_address_put_request import AmazonPaymentAddressManagementV1GetBillingAddressPutRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_amazon_payment_address_management_v1_get_shipping_address_put(client):
    """Test case for amazon_payment_address_management_v1_get_shipping_address_put

    amazon-shipping-address/{amazonOrderReferenceId}
    """
    body = openapi_server.AmazonPaymentAddressManagementV1GetBillingAddressPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/amazon-shipping-address/{amazon_order_reference_id}'.format(amazon_order_reference_id='amazon_order_reference_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

