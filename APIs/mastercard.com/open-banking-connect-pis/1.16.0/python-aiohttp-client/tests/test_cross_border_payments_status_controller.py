# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_cross_border_credit_transfers_payment_status_ok_body import PostPaymentsCrossBorderCreditTransfersPaymentStatusOKBody
from openapi_server.models.post_payments_cross_border_credit_transfers_payment_status_params_body import PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody


pytestmark = pytest.mark.asyncio

async def test_payments_cross_border_credit_transfers_payment_status_post(client):
    """Test case for payments_cross_border_credit_transfers_payment_status_post

    Get payment status
    """
    body = openapi_server.PostPaymentsCrossBorderCreditTransfersPaymentStatusParamsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/openbanking/sandbox/connect/api/payments/cross-border-credit-transfers/payment-status',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

