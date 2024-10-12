# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.register_account_request_body import RegisterAccountRequestBody
from openapi_server.models.request_code_request_body import RequestCodeRequestBody
from openapi_server.models.request_code_response import RequestCodeResponse


pytestmark = pytest.mark.asyncio

async def test_register_account(client):
    """Test case for register_account

    Register-Account
    """
    body = {"code":"<Registration Code Received via SMS/Voice>"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/account/verify',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_code(client):
    """Test case for request_code

    Request-Code
    """
    body = {"cc":"<Country Code>","cert":"<Valid Cert from Business Manager>","method":"sms","phone_number":"<Phone Number>","pin":"<Two-Step Verification PIN"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/account',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

