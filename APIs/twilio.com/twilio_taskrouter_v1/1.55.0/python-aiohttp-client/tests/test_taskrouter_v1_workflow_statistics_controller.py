# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.taskrouter_v1_workspace_workflow_workflow_statistics import TaskrouterV1WorkspaceWorkflowWorkflowStatistics


pytestmark = pytest.mark.asyncio

async def test_fetch_workflow_statistics(client):
    """Test case for fetch_workflow_statistics

    
    """
    params = [('Minutes', 56),
                    ('StartDate', '2013-10-20T19:20:30+01:00'),
                    ('EndDate', '2013-10-20T19:20:30+01:00'),
                    ('TaskChannel', 'task_channel_example'),
                    ('SplitByWaitTime', 'split_by_wait_time_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Workflows/{workflow_sid}/Statistics'.format(workspace_sid='workspace_sid_example', workflow_sid='workflow_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

