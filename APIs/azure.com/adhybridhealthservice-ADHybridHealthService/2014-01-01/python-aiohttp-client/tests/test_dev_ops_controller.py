# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.result import Result


pytestmark = pytest.mark.asyncio

async def test_reports_get_dev_ops(client):
    """Test case for reports_get_dev_ops

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/reports/DevOps/IsDevOps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

