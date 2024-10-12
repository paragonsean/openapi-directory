# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_customer_balance_balance_management_from_quote_v1_unapply_post(client):
    """Test case for customer_balance_balance_management_from_quote_v1_unapply_post

    carts/mine/balance/unapply
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/carts/mine/balance/unapply',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

