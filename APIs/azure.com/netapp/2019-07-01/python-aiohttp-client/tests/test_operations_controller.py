# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_list_result import OperationListResult


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    Describes the Resource Provider
    """
    params = [('api-version', '2019-07-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.NetApp/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

