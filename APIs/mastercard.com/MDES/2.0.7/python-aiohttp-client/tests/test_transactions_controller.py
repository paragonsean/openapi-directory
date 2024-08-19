# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.transactions_request_schema import TransactionsRequestSchema
from openapi_server.models.transactions_response_schema import TransactionsResponseSchema


pytestmark = pytest.mark.asyncio

async def test_transactions_post(client):
    """Test case for transactions_post

    
    """
    transactions_request_schema = {"TransactionsRequest":{"TokenUniqueReference":"DWSPMC00000000010906a349d9ca4eb1a4d53e3c90a11d9c","AuditInfo":{"Organization":"Solid Bank Inc","UserName":"John Smith","Phone":"5555551234","UserId":"A1435477"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/mdes/csapi/v2/transactions',
        headers=headers,
        json=transactions_request_schema,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

