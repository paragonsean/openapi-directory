# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_sepa_credit_transfers_consents_ok_body import PostPaymentsSepaCreditTransfersConsentsOKBody
from openapi_server.models.post_payments_sepa_credit_transfers_consents_params_body import PostPaymentsSepaCreditTransfersConsentsParamsBody


pytestmark = pytest.mark.asyncio

async def test_payments_sepa_credit_transfers_consents_post(client):
    """Test case for payments_sepa_credit_transfers_consents_post

    Request consent initiation via redirect
    """
    body = openapi_server.PostPaymentsSepaCreditTransfersConsentsParamsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/openbanking/sandbox/connect/api/payments/sepa-credit-transfers/consents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

