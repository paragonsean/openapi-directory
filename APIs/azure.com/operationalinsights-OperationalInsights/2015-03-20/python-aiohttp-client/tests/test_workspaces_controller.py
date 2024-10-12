# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.link_target import LinkTarget
from openapi_server.models.search_get_schema_response import SearchGetSchemaResponse
from openapi_server.models.shared_keys import SharedKeys
from openapi_server.models.workspace_purge_body import WorkspacePurgeBody
from openapi_server.models.workspace_purge_response import WorkspacePurgeResponse
from openapi_server.models.workspace_purge_status_response import WorkspacePurgeStatusResponse


pytestmark = pytest.mark.asyncio

async def test_workspaces_delete_gateways(client):
    """Test case for workspaces_delete_gateways

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/gateways/{gateway_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', gateway_id='gateway_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_get_purge_status(client):
    """Test case for workspaces_get_purge_status

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/operations/{purge_id}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', workspace_name='workspace_name_example', purge_id='purge_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_get_schema(client):
    """Test case for workspaces_get_schema

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/schema'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_list_keys(client):
    """Test case for workspaces_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/listKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_list_link_targets(client):
    """Test case for workspaces_list_link_targets

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.OperationalInsights/linkTargets'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_purge(client):
    """Test case for workspaces_purge

    
    """
    body = {"filters":[{"column":"column","value":"{}","key":"key","operator":"operator"},{"column":"column","value":"{}","key":"key","operator":"operator"}],"table":"table"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/purge'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', workspace_name='workspace_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workspaces_regenerate_shared_keys(client):
    """Test case for workspaces_regenerate_shared_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/regenerateSharedKey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

