# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.studio_v1_flow_execution_execution_context import StudioV1FlowExecutionExecutionContext


pytestmark = pytest.mark.asyncio

async def test_fetch_execution_context(client):
    """Test case for fetch_execution_context

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Flows/{flow_sid}/Executions/{execution_sid}/Context'.format(flow_sid='flow_sid_example', execution_sid='execution_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

