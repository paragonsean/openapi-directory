# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.serverless_v1_service_function_function_version_function_version_content import ServerlessV1ServiceFunctionFunctionVersionFunctionVersionContent


pytestmark = pytest.mark.asyncio

async def test_fetch_function_version_content(client):
    """Test case for fetch_function_version_content

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}/Content'.format(service_sid='service_sid_example', function_sid='function_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

