# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_task_queue_response import ListTaskQueueResponse
from openapi_server.models.task_queue_enum_task_order import TaskQueueEnumTaskOrder
from openapi_server.models.taskrouter_v1_workspace_task_queue import TaskrouterV1WorkspaceTaskQueue


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_task_queue(client):
    """Test case for create_task_queue

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'assignment_activity_sid': 'assignment_activity_sid_example',
        'friendly_name': 'friendly_name_example',
        'max_reserved_workers': 56,
        'reservation_activity_sid': 'reservation_activity_sid_example',
        'target_workers': 'target_workers_example',
        'task_order': openapi_server.TaskQueueEnumTaskOrder()
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/TaskQueues'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_task_queue(client):
    """Test case for delete_task_queue

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_task_queue(client):
    """Test case for fetch_task_queue

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_task_queue(client):
    """Test case for list_task_queue

    
    """
    params = [('FriendlyName', 'friendly_name_example'),
                    ('EvaluateWorkerAttributes', 'evaluate_worker_attributes_example'),
                    ('WorkerSid', 'worker_sid_example'),
                    ('Ordering', 'ordering_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/TaskQueues'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_task_queue(client):
    """Test case for update_task_queue

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'assignment_activity_sid': 'assignment_activity_sid_example',
        'friendly_name': 'friendly_name_example',
        'max_reserved_workers': 56,
        'reservation_activity_sid': 'reservation_activity_sid_example',
        'target_workers': 'target_workers_example',
        'task_order': openapi_server.TaskQueueEnumTaskOrder()
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/TaskQueues/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

