# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_task_response import ListTaskResponse
from openapi_server.models.task_enum_status import TaskEnumStatus
from openapi_server.models.taskrouter_v1_workspace_task import TaskrouterV1WorkspaceTask


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_task(client):
    """Test case for create_task

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'attributes': 'attributes_example',
        'priority': 56,
        'task_channel': 'task_channel_example',
        'timeout': 56,
        'virtual_start_time': '2013-10-20T19:20:30+01:00',
        'workflow_sid': 'workflow_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/Tasks'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_task(client):
    """Test case for delete_task

    
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Workspaces/{workspace_sid}/Tasks/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_task(client):
    """Test case for fetch_task

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Tasks/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_task(client):
    """Test case for list_task

    
    """
    params = [('Priority', 56),
                    ('AssignmentStatus', ['assignment_status_example']),
                    ('WorkflowSid', 'workflow_sid_example'),
                    ('WorkflowName', 'workflow_name_example'),
                    ('TaskQueueSid', 'task_queue_sid_example'),
                    ('TaskQueueName', 'task_queue_name_example'),
                    ('EvaluateTaskAttributes', 'evaluate_task_attributes_example'),
                    ('Ordering', 'ordering_example'),
                    ('HasAddons', True),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Tasks'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_task(client):
    """Test case for update_task

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'assignment_status': openapi_server.TaskEnumStatus(),
        'attributes': 'attributes_example',
        'priority': 56,
        'reason': 'reason_example',
        'task_channel': 'task_channel_example',
        'virtual_start_time': '2013-10-20T19:20:30+01:00'
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/Tasks/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

