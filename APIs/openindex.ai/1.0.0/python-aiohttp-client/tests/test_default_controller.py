# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_response import QueryResponse


pytestmark = pytest.mark.asyncio

async def test_query_query_post(client):
    """Test case for query_query_post

    Query
    """
    body = {"namespace":"namespace","queries":[{"filter":{"collection_id":"collection_id","end_date":"end_date","keywords":["keywords","keywords"],"user_id":"user_id","author":"author","language":"language","source":"email","source_id":"source_id","document_id":"document_id","time_period":"time_period","start_date":"start_date"},"query":"query","top_k":0},{"filter":{"collection_id":"collection_id","end_date":"end_date","keywords":["keywords","keywords"],"user_id":"user_id","author":"author","language":"language","source":"email","source_id":"source_id","document_id":"document_id","time_period":"time_period","start_date":"start_date"},"query":"query","top_k":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sub/query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

