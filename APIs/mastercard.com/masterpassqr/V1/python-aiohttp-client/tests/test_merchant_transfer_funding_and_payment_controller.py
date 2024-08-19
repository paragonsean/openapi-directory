# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.merchant_transfer14_wrapper import MerchantTransfer14Wrapper
from openapi_server.models.merchant_transfer1_wrapper import MerchantTransfer1Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_merchant_transfer(client):
    """Test case for create_merchant_transfer

    Initiates a Mastercard Merchant Presented QR purchase transaction by securing funds from a consumer’s account with a Funding Transaction and pushing funds to a merchant account with a Payment Transaction.
    """
    merchant_transfer = openapi_server.MerchantTransfer1Wrapper()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/send/#env/v1/partners/{partner_id}/merchant/transfer'.format(partner_id='ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9'),
        headers=headers,
        json=merchant_transfer,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

