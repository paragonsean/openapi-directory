# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_quote_coupon_management_v1_set_put(client):
    """Test case for quote_coupon_management_v1_set_put

    carts/mine/coupons/{couponCode}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/carts/mine/coupons/{coupon_code}'.format(coupon_code='coupon_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

