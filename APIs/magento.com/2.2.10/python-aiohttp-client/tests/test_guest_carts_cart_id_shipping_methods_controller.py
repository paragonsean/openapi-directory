# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.quote_data_shipping_method_interface import QuoteDataShippingMethodInterface


pytestmark = pytest.mark.asyncio

async def test_quote_guest_shipping_method_management_v1_get_list_get(client):
    """Test case for quote_guest_shipping_method_management_v1_get_list_get

    guest-carts/{cartId}/shipping-methods
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/guest-carts/{cart_id}/shipping-methods'.format(cart_id='cart_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

