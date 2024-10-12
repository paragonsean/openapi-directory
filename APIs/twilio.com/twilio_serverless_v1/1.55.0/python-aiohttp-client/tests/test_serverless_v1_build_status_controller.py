# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.serverless_v1_service_build_build_status import ServerlessV1ServiceBuildBuildStatus


pytestmark = pytest.mark.asyncio

async def test_fetch_build_status(client):
    """Test case for fetch_build_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Builds/{sid}/Status'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

