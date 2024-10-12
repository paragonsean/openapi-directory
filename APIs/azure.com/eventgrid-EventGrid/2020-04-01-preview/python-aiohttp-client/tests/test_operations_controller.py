# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operations_list_result import OperationsListResult


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    List available operations.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.EventGrid/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

