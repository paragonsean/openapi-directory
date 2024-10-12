# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance_transfer_request import BalanceTransferRequest
from openapi_server.models.balance_transfer_response import BalanceTransferResponse


pytestmark = pytest.mark.asyncio

async def test_post_balance_transfer(client):
    """Test case for post_balance_transfer

    Start a balance transfer
    """
    body = {"reference":"reference","amount":{"currency":"currency","value":0},"fromMerchant":"fromMerchant","description":"description","toMerchant":"toMerchant","type":"tax"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/servlet/BalanceControl/v1/balanceTransfer',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

