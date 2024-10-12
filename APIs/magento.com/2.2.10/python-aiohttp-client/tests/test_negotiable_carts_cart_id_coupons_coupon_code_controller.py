# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_negotiable_quote_coupon_management_v1_set_put(client):
    """Test case for negotiable_quote_coupon_management_v1_set_put

    negotiable-carts/{cartId}/coupons/{couponCode}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/negotiable-carts/{cart_id}/coupons/{coupon_code}'.format(cart_id=56, coupon_code='coupon_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

