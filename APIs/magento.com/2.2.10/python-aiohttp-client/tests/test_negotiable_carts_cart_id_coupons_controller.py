# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_negotiable_quote_coupon_management_v1_remove_delete(client):
    """Test case for negotiable_quote_coupon_management_v1_remove_delete

    negotiable-carts/{cartId}/coupons
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/negotiable-carts/{cart_id}/coupons'.format(cart_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

