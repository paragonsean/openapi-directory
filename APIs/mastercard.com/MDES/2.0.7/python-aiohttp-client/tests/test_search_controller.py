# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.search_request_schema import SearchRequestSchema
from openapi_server.models.search_response_schema import SearchResponseSchema


pytestmark = pytest.mark.asyncio

async def test_search_post(client):
    """Test case for search_post

    
    """
    search_request_schema = {"SearchRequest":{"TokenUniqueReference":"DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c","AuditInfo":{"Organization":"Solid Bank Inc","UserName":"John Smith","Phone":"5555551234","UserId":"A1435477"},"PaymentAppInstanceId":"645b532a245e4723d7a9c4f62b24f24a24ba98e27d43e34e","ExcludeDeletedIndicator":"true","Token":"5598765432109876","AlternateAccountIdentifier":"NL91ABNA0417164300","AccountPan":"5412345678901234","CommentId":"123456"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/mdes/csapi/v2/search',
        headers=headers,
        json=search_request_schema,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

