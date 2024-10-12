# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.studio_v2_flow_execution_execution_step_execution_step_context import StudioV2FlowExecutionExecutionStepExecutionStepContext


pytestmark = pytest.mark.asyncio

async def test_fetch_execution_step_context(client):
    """Test case for fetch_execution_step_context

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{step_sid}/Context'.format(flow_sid='flow_sid_example', execution_sid='execution_sid_example', step_sid='step_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

