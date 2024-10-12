# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_workflow_response import ListWorkflowResponse
from openapi_server.models.taskrouter_v1_workspace_workflow import TaskrouterV1WorkspaceWorkflow


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_workflow(client):
    """Test case for create_workflow

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'assignment_callback_url': 'assignment_callback_url_example',
        'configuration': 'configuration_example',
        'fallback_assignment_callback_url': 'fallback_assignment_callback_url_example',
        'friendly_name': 'friendly_name_example',
        'task_reservation_timeout': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/Workflows'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_workflow(client):
    """Test case for delete_workflow

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Workspaces/{workspace_sid}/Workflows/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_workflow(client):
    """Test case for fetch_workflow

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Workflows/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_workflow(client):
    """Test case for list_workflow

    
    """
    params = [('FriendlyName', 'friendly_name_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Workflows'.format(workspace_sid='workspace_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_workflow(client):
    """Test case for update_workflow

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'assignment_callback_url': 'assignment_callback_url_example',
        'configuration': 'configuration_example',
        'fallback_assignment_callback_url': 'fallback_assignment_callback_url_example',
        'friendly_name': 'friendly_name_example',
        're_evaluate_tasks': 're_evaluate_tasks_example',
        'task_reservation_timeout': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/Workflows/{sid}'.format(workspace_sid='workspace_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

