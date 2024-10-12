# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.merchant_payment_transfer29_wrapper import MerchantPaymentTransfer29Wrapper
from openapi_server.models.merchant_transfer40_wrapper import MerchantTransfer40Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_merchant_payment(client):
    """Test case for create_merchant_payment

    Initiates a Mastercard Merchant Presented QR purchase transaction by pushing funds to a merchant account.
    """
    merchant_payment_transfer = openapi_server.MerchantPaymentTransfer29Wrapper()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/send/#env/v1/partners/{partner_id}/merchant/transfers/payment'.format(partner_id='partner_id_example'),
        headers=headers,
        json=merchant_payment_transfer,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

