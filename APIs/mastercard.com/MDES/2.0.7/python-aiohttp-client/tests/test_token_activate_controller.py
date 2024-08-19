# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_activate_request_schema import TokenActivateRequestSchema
from openapi_server.models.token_activate_response_schema import TokenActivateResponseSchema


pytestmark = pytest.mark.asyncio

async def test_token_activate_post(client):
    """Test case for token_activate_post

    
    """
    token_activate_request_schema = {"TokenActivateRequest":{"TokenUniqueReference":"DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c","AuditInfo":{"Organization":"Solid Bank Inc","UserName":"John Smith","Phone":"5555551234","UserId":"A1435477"},"PaymentAppInstanceId":"645b532a245e4723d7a9c4f62b24f24a24ba98e27d43e34e","CommentText":"activated after confirming cardholder identity","ReasonCode":"A","AccountPan":"5412345678901234"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/mdes/csapi/v2/token/activate',
        headers=headers,
        json=token_activate_request_schema,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

