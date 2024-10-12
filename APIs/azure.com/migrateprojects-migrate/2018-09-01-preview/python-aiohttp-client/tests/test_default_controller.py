# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_result_list import OperationResultList


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    Get list of operations supported in the API.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Migrate/operations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

