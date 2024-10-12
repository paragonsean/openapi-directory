# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_update_request_schema import TokenUpdateRequestSchema
from openapi_server.models.token_update_response_schema import TokenUpdateResponseSchema


pytestmark = pytest.mark.asyncio

async def test_token_update_post(client):
    """Test case for token_update_post

    
    """
    token_update_request_schema = {"TokenUpdateRequest":{"TokenUniqueReference":"DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c","NewAccountPan":"5412345678908888","AuditInfo":{"Organization":"Solid Bank Inc","UserName":"John Smith","Phone":"5555551234","UserId":"A1435477"},"AccountPanSequenceNumber":"59","ExpirationDate":"1225","CurrentAccountPan":"5412345678901234","CommentText":"Update gold artwork","IssuerProductConfigurationId":"ANYGOLD101","UpdateWalletProviderIndicator":"0"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/mdes/csapi/v2/token/update',
        headers=headers,
        json=token_update_request_schema,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

