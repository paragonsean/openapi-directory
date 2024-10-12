# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_inputs_response import GetAllInputsResponse


pytestmark = pytest.mark.asyncio

async def test_get_all_inputs(client):
    """Test case for get_all_inputs

    Get all inputs you have access to
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/inputs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

