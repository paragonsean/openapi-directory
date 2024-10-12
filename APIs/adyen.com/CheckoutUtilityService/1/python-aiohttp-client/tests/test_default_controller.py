# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.checkout_utility_request import CheckoutUtilityRequest
from openapi_server.models.checkout_utility_response import CheckoutUtilityResponse


pytestmark = pytest.mark.asyncio

async def test_origin_keys_post(client):
    """Test case for origin_keys_post

    Create originKey values for one or more merchant domains.
    """
    body = {"originDomains":["originDomains","originDomains"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/originKeys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

