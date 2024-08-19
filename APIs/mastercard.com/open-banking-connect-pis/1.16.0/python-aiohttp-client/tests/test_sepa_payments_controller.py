# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_sepa_credit_transfers_ok_body import PostPaymentsSepaCreditTransfersOKBody
from openapi_server.models.post_payments_sepa_credit_transfers_params_body import PostPaymentsSepaCreditTransfersParamsBody


pytestmark = pytest.mark.asyncio

async def test_payments_sepa_credit_transfers_post(client):
    """Test case for payments_sepa_credit_transfers_post

    Redeem the payment
    """
    body = openapi_server.PostPaymentsSepaCreditTransfersParamsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/openbanking/sandbox/connect/api/payments/sepa-credit-transfers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

