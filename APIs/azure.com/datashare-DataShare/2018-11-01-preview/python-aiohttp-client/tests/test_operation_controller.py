# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.operation_list import OperationList


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    Lists the available operations
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.DataShare/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

