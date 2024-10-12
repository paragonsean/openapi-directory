# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_worker_channel_response import ListWorkerChannelResponse
from openapi_server.models.taskrouter_v1_workspace_worker_worker_channel import TaskrouterV1WorkspaceWorkerWorkerChannel


pytestmark = pytest.mark.asyncio

async def test_fetch_worker_channel(client):
    """Test case for fetch_worker_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels/{sid}'.format(workspace_sid='workspace_sid_example', worker_sid='worker_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_worker_channel(client):
    """Test case for list_worker_channel

    
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
        path='/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels'.format(workspace_sid='workspace_sid_example', worker_sid='worker_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_worker_channel(client):
    """Test case for update_worker_channel

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'available': True,
        'capacity': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels/{sid}'.format(workspace_sid='workspace_sid_example', worker_sid='worker_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

