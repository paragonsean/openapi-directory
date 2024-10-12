# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_resend_activation_code_request_schema import TokenResendActivationCodeRequestSchema
from openapi_server.models.token_resend_activation_code_response_schema import TokenResendActivationCodeResponseSchema


pytestmark = pytest.mark.asyncio

async def test_token_resendactivationcode_post(client):
    """Test case for token_resendactivationcode_post

    
    """
    token_resend_activation_code_request_schema = {"TokenResendActivationCodeRequest":{"TokenUniqueReference":"DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c","AuditInfo":{"Organization":"Solid Bank Inc","UserName":"John Smith","Phone":"5555551234","UserId":"A1435477"},"ActivationMethodId":"123123122"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/mdes/csapi/v2/token/resendactivationcode',
        headers=headers,
        json=token_resend_activation_code_request_schema,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

