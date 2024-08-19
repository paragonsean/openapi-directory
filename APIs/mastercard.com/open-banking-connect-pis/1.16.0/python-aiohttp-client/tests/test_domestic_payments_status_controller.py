# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_domestic_credit_transfers_payment_status_ok_body import PostPaymentsDomesticCreditTransfersPaymentStatusOKBody
from openapi_server.models.post_payments_domestic_credit_transfers_payment_status_params_body import PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody


pytestmark = pytest.mark.asyncio

async def test_payments_domestic_credit_transfers_payment_status_post(client):
    """Test case for payments_domestic_credit_transfers_payment_status_post

    Get payment status
    """
    body = openapi_server.PostPaymentsDomesticCreditTransfersPaymentStatusParamsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/openbanking/sandbox/connect/api/payments/domestic-credit-transfers/payment-status',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

