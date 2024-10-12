# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_function_version_response import ListFunctionVersionResponse
from openapi_server.models.serverless_v1_service_function_function_version import ServerlessV1ServiceFunctionFunctionVersion


pytestmark = pytest.mark.asyncio

async def test_fetch_function_version(client):
    """Test case for fetch_function_version

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}'.format(service_sid='service_sid_example', function_sid='function_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_function_version(client):
    """Test case for list_function_version

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Functions/{function_sid}/Versions'.format(service_sid='service_sid_example', function_sid='function_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

