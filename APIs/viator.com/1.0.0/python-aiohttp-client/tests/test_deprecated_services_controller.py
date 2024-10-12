# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.merchant_cancellation200_response import MerchantCancellation200Response
from openapi_server.models.merchant_cancellation400_response import MerchantCancellation400Response
from openapi_server.models.merchant_cancellation_request import MerchantCancellationRequest


pytestmark = pytest.mark.asyncio

async def test_merchant_cancellation(client):
    """Test case for merchant_cancellation

    /merchant/cancellation
    """
    body = openapi_server.MerchantCancellationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/merchant/cancellation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

