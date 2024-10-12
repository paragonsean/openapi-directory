# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.available_operations import AvailableOperations


pytestmark = pytest.mark.asyncio

async def test_machine_learning_compute_list_available_operations(client):
    """Test case for machine_learning_compute_list_available_operations

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.MachineLearningCompute/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

