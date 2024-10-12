# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_payload_schema import BatchPayloadSchema
from openapi_server.models.batch_response_body_schema import BatchResponseBodySchema
from openapi_server.models.error_schema import ErrorSchema


pytestmark = pytest.mark.asyncio

async def test_batch(client):
    """Test case for batch

    
    """
    body = {"defaults":{"headers":{"key":""},"path":"path","method":"GET","body":{"key":""}},"requests":[{"headers":{"key":""},"path":"path","method":"GET","body":{"key":""}},{"headers":{"key":""},"path":"path","method":"GET","body":{"key":""}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

