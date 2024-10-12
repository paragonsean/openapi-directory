# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.verify_payout_request import VerifyPayoutRequest


pytestmark = pytest.mark.asyncio

async def test_verify_payout(client):
    """Test case for verify_payout

    Verify payout
    """
    body = {"verification_code":"123456"}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'x_api_key': '{{your_api_key}}',
    }
    response = await client.request(
        method='POST',
        path='/v1/payout/{withdrawals_id}/verify'.format(withdrawals_id='5000000191'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

