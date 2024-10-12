# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_domestic_credit_transfers_consents_ok_body import PostPaymentsDomesticCreditTransfersConsentsOKBody
from openapi_server.models.post_payments_domestic_credit_transfers_consents_params_body import PostPaymentsDomesticCreditTransfersConsentsParamsBody


pytestmark = pytest.mark.asyncio

async def test_payments_domestic_credit_transfers_consents_post(client):
    """Test case for payments_domestic_credit_transfers_consents_post

    Request consent initiation via redirect
    """
    body = openapi_server.PostPaymentsDomesticCreditTransfersConsentsParamsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/openbanking/sandbox/connect/api/payments/domestic-credit-transfers/consents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

