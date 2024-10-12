# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_batch_request200_response import CreateBatchRequest200Response
from openapi_server.models.create_batch_request_request import CreateBatchRequestRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_create_batch_request(client):
    """Test case for create_batch_request

    Submit parallel requests
    """
    body = openapi_server.CreateBatchRequestRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/batch',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

