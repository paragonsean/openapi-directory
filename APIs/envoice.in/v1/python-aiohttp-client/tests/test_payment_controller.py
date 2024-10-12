# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.payment_gateway_details_api_model import PaymentGatewayDetailsApiModel


pytestmark = pytest.mark.asyncio

async def test_payment_api_supported(client):
    """Test case for payment_api_supported

    Return all supported payment gateways (no currencies means all are supported)
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_key': '[authentication key]',
        'x_auth_secret': '[authentication secret]',
    }
    response = await client.request(
        method='GET',
        path='/api/payment/supported',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

