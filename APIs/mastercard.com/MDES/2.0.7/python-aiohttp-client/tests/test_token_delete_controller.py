# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_delete_request_schema import TokenDeleteRequestSchema
from openapi_server.models.token_delete_response_schema import TokenDeleteResponseSchema


pytestmark = pytest.mark.asyncio

async def test_token_delete_post(client):
    """Test case for token_delete_post

    
    """
    token_delete_request_schema = {"TokenDeleteRequest":{"TokenUniqueReference":"DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c","AuditInfo":{"Organization":"Solid Bank Inc","UserName":"John Smith","Phone":"5555551234","UserId":"A1435477"},"CommentText":"Cardholder reported fraudulent transactions.","ReasonCode":"C"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/mdes/csapi/v2/token/delete',
        headers=headers,
        json=token_delete_request_schema,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

