# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_request_response import AddRequestResponse
from openapi_server.models.create_payment_request import CreatePaymentRequest
from openapi_server.models.payment_request_state_response import PaymentRequestStateResponse


pytestmark = pytest.mark.asyncio

async def test_add_payment_request(client):
    """Test case for add_payment_request

    Creates a new payment request. Will return request id to check for transaction state and ergopay url to show the user as QR code
    """
    body = {"receiverAddress":"receiverAddress","senderAddress":"senderAddress","nanoErg":0,"tokenId":"tokenId","message":"message","tokenRawAmount":6}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/payment/addrequest',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payment_state(client):
    """Test case for get_payment_state

    Returns the state of a payment request. Please note that payment requests are purged after some time, so persist the state at your side when needed
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/payment/state/{request_id}'.format(request_id='request_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

