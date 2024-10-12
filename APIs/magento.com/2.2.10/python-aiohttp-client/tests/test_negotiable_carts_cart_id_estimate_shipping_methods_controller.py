# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_shipping_method_interface import QuoteDataShippingMethodInterface
from openapi_server.models.quote_shipment_estimation_v1_estimate_by_extended_address_post_request import QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_negotiable_quote_shipment_estimation_v1_estimate_by_extended_address_post(client):
    """Test case for negotiable_quote_shipment_estimation_v1_estimate_by_extended_address_post

    negotiable-carts/{cartId}/estimate-shipping-methods
    """
    body = openapi_server.QuoteShipmentEstimationV1EstimateByExtendedAddressPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/negotiable-carts/{cart_id}/estimate-shipping-methods'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

