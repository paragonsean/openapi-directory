# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_payment_account_reference_request_schema import GetPaymentAccountReferenceRequestSchema
from openapi_server.models.get_payment_account_reference_response_schema import GetPaymentAccountReferenceResponseSchema


pytestmark = pytest.mark.asyncio

async def test_par_paymentaccountreference10_get_payment_account_reference_post(client):
    """Test case for par_paymentaccountreference10_get_payment_account_reference_post

    Submit an encrypted PAN to obtain the PAR linked to the account.
    """
    get_payment_account_reference_request_schema = openapi_server.GetPaymentAccountReferenceRequestSchema()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/par/paymentaccountreference/1/0/getPaymentAccountReference',
        headers=headers,
        json=get_payment_account_reference_request_schema,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

