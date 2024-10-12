# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_v1_carts_cart_id_coupons_coupon_code_put(client):
    """Test case for v1_carts_cart_id_coupons_coupon_code_put

    carts/{cartId}/coupons/{couponCode}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/carts/{cart_id}/coupons/{coupon_code}'.format(cart_id=56, coupon_code='coupon_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

