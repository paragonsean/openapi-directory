# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_cross_border_credit_transfers_ok_body import PostPaymentsCrossBorderCreditTransfersOKBody
from openapi_server.models.post_payments_cross_border_credit_transfers_params_body import PostPaymentsCrossBorderCreditTransfersParamsBody


pytestmark = pytest.mark.asyncio

async def test_payments_cross_border_credit_transfers_post(client):
    """Test case for payments_cross_border_credit_transfers_post

    Redeem the payment
    """
    body = openapi_server.PostPaymentsCrossBorderCreditTransfersParamsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/openbanking/sandbox/connect/api/payments/cross-border-credit-transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

