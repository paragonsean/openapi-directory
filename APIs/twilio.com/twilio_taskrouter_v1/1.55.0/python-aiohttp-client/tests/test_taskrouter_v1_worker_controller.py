# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_worker_response import ListWorkerResponse
from openapi_server.models.taskrouter_v1_workspace_worker import TaskrouterV1WorkspaceWorker


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_worker(client):
    """Test case for create_worker

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'activity_sid': 'activity_sid_example',
        'attributes': 'attributes_example',
        'friendly_name': 'friendly_name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/Workers'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_worker(client):
    """Test case for delete_worker

    
    """
    headers = { 
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Workspaces/{workspace_sid}/Workers/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_worker(client):
    """Test case for fetch_worker

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Workers/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_worker(client):
    """Test case for list_worker

    
    """
    params = [('ActivityName', 'activity_name_example'),
                    ('ActivitySid', 'activity_sid_example'),
                    ('Available', 'available_example'),
                    ('FriendlyName', 'friendly_name_example'),
                    ('TargetWorkersExpression', 'target_workers_expression_example'),
                    ('TaskQueueName', 'task_queue_name_example'),
                    ('TaskQueueSid', 'task_queue_sid_example'),
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
        path='/v1/Workspaces/{workspace_sid}/Workers'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_worker(client):
    """Test case for update_worker

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'if_match': 'if_match_example',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'activity_sid': 'activity_sid_example',
        'attributes': 'attributes_example',
        'friendly_name': 'friendly_name_example',
        'reject_pending_reservations': True
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/Workers/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

