# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.post_payments_cross_border_credit_transfers_consents_ok_body import PostPaymentsCrossBorderCreditTransfersConsentsOKBody
from openapi_server.models.post_payments_cross_border_credit_transfers_consents_params_body import PostPaymentsCrossBorderCreditTransfersConsentsParamsBody


pytestmark = pytest.mark.asyncio

async def test_payments_cross_border_credit_transfers_consents_post(client):
    """Test case for payments_cross_border_credit_transfers_consents_post

    Request consent initiation via redirect
    """
    body = openapi_server.PostPaymentsCrossBorderCreditTransfersConsentsParamsBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/openbanking/sandbox/connect/api/payments/cross-border-credit-transfers/consents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

