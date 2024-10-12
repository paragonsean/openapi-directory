# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_rule_coupon_management_v1_generate_post_request import SalesRuleCouponManagementV1GeneratePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_rule_coupon_management_v1_generate_post(client):
    """Test case for sales_rule_coupon_management_v1_generate_post

    coupons/generate
    """
    body = openapi_server.SalesRuleCouponManagementV1GeneratePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/coupons/generate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

