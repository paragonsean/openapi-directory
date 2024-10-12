# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_operations_get_details(client):
    """Test case for operations_get_details

    Gets details of a specific long running operation.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/operations/{operation_id}'.format(operation_id='operation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

