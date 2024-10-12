# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_execution_step_response import ListExecutionStepResponse
from openapi_server.models.studio_v2_flow_execution_execution_step import StudioV2FlowExecutionExecutionStep


pytestmark = pytest.mark.asyncio

async def test_fetch_execution_step(client):
    """Test case for fetch_execution_step

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{sid}'.format(flow_sid='flow_sid_example', execution_sid='execution_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_execution_step(client):
    """Test case for list_execution_step

    
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
        path='/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps'.format(flow_sid='flow_sid_example', execution_sid='execution_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

