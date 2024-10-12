# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.merchant_refund_transfer93_wrapper import MerchantRefundTransfer93Wrapper
from openapi_server.models.merchant_transfer104_wrapper import MerchantTransfer104Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_merchant_refund(client):
    """Test case for create_merchant_refund

    Initiates a Mastercard Merchant Presented QR Refund transaction by pushing funds from a merchant account back to the customer's account.
    """
    merchant_refund_transfer = openapi_server.MerchantRefundTransfer93Wrapper()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/send/#env/v1/partners/{partner_id}/merchant/transfers/refund'.format(partner_id='partner_id_example'),
        headers=headers,
        json=merchant_refund_transfer,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

