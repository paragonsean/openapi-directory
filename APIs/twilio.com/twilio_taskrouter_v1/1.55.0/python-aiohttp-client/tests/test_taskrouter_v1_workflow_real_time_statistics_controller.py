# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.taskrouter_v1_workspace_workflow_workflow_real_time_statistics import TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics


pytestmark = pytest.mark.asyncio

async def test_fetch_workflow_real_time_statistics(client):
    """Test case for fetch_workflow_real_time_statistics

    
    """
    params = [('TaskChannel', 'task_channel_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/RealTimeStatistics'.format(workspace_sid='workspace_sid_example', workflow_sid='workflow_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

