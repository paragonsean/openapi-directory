# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.condition import Condition
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_get_condition(client):
    """Test case for get_condition

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/conditions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

