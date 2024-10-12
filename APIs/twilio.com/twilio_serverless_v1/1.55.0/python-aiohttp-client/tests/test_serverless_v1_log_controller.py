# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_log_response import ListLogResponse
from openapi_server.models.serverless_v1_service_environment_log import ServerlessV1ServiceEnvironmentLog


pytestmark = pytest.mark.asyncio

async def test_fetch_log(client):
    """Test case for fetch_log

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Environments/{environment_sid}/Logs/{sid}'.format(service_sid='service_sid_example', environment_sid='environment_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_log(client):
    """Test case for list_log

    
    """
    params = [('FunctionSid', 'function_sid_example'),
                    ('StartDate', '2013-10-20T19:20:30+01:00'),
                    ('EndDate', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Environments/{environment_sid}/Logs'.format(service_sid='service_sid_example', environment_sid='environment_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

