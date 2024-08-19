# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bill_pay_request import BillPayRequest
from openapi_server.models.bill_pay_response import BillPayResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/JSON not supported by Connexion")
async def test_is_routing_valid_post(client):
    """Test case for is_routing_valid_post

    Bill Payment Validator service returns the processing status for a potential RPPS transaction
    """
    bill_pay_request = openapi_server.BillPayRequest()
    headers = { 
        'Accept': 'application/JSON',
        'Content-Type': 'application/JSON',
    }
    response = await client.request(
        method='POST',
        path='/billpayAPI/v1/isRoutingValid',
        headers=headers,
        json=bill_pay_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

