# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.logs_request_body import LogsRequestBody
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo


pytestmark = pytest.mark.asyncio

async def test_get_logs(client):
    """Test case for get_logs

    Get logs
    """
    body = {"logType":"server"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/logs/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

