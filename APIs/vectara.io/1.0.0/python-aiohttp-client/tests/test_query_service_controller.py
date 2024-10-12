# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.googlerpc_status import GooglerpcStatus
from openapi_server.models.serving_batch_query_request import ServingBatchQueryRequest
from openapi_server.models.serving_batch_query_response import ServingBatchQueryResponse
from openapi_server.models.stream_result_of_serving_response_set import StreamResultOfServingResponseSet


pytestmark = pytest.mark.asyncio

async def test_query(client):
    """Test case for query

    
    """
    body = openapi_server.ServingBatchQueryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'customer_id': 56,
        'ApiKeyAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stream_query(client):
    """Test case for stream_query

    
    """
    body = openapi_server.ServingBatchQueryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'customer_id': 56,
        'ApiKeyAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/stream-query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

