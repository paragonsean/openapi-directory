# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.workspace_setting import WorkspaceSetting
from openapi_server.models.workspace_setting_list import WorkspaceSettingList


pytestmark = pytest.mark.asyncio

async def test_workspace_settings_create(client):
    """Test case for workspace_settings_create

    
    """
    workspace_setting = {"properties":{"scope":"scope","workspaceId":"workspaceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/workspaceSettings/{workspace_setting_name}'.format(subscription_id='subscription_id_example', workspace_setting_name='workspace_setting_name_example'),
        headers=headers,
        json=workspace_setting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_settings_delete(client):
    """Test case for workspace_settings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/workspaceSettings/{workspace_setting_name}'.format(subscription_id='subscription_id_example', workspace_setting_name='workspace_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_settings_get(client):
    """Test case for workspace_settings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/workspaceSettings/{workspace_setting_name}'.format(subscription_id='subscription_id_example', workspace_setting_name='workspace_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_settings_list(client):
    """Test case for workspace_settings_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/workspaceSettings'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspace_settings_update(client):
    """Test case for workspace_settings_update

    
    """
    workspace_setting = {"properties":{"scope":"scope","workspaceId":"workspaceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/workspaceSettings/{workspace_setting_name}'.format(subscription_id='subscription_id_example', workspace_setting_name='workspace_setting_name_example'),
        headers=headers,
        json=workspace_setting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

