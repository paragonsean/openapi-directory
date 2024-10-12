# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_workspace_response import ListWorkspaceResponse
from openapi_server.models.taskrouter_v1_workspace import TaskrouterV1Workspace
from openapi_server.models.workspace_enum_queue_order import WorkspaceEnumQueueOrder


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_workspace(client):
    """Test case for create_workspace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'event_callback_url': 'event_callback_url_example',
        'events_filter': 'events_filter_example',
        'friendly_name': 'friendly_name_example',
        'multi_task_enabled': True,
        'prioritize_queue_order': openapi_server.WorkspaceEnumQueueOrder(),
        'template': 'template_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_workspace(client):
    """Test case for delete_workspace

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Workspaces/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_workspace(client):
    """Test case for fetch_workspace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_workspace(client):
    """Test case for list_workspace

    
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
        path='/v1/Workspaces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_workspace(client):
    """Test case for update_workspace

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'default_activity_sid': 'default_activity_sid_example',
        'event_callback_url': 'event_callback_url_example',
        'events_filter': 'events_filter_example',
        'friendly_name': 'friendly_name_example',
        'multi_task_enabled': True,
        'prioritize_queue_order': openapi_server.WorkspaceEnumQueueOrder(),
        'timeout_activity_sid': 'timeout_activity_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

