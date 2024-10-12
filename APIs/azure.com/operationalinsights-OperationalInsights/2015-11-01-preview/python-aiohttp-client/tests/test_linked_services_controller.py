# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.linked_service import LinkedService
from openapi_server.models.linked_service_list_result import LinkedServiceListResult


pytestmark = pytest.mark.asyncio

async def test_linked_services_create_or_update(client):
    """Test case for linked_services_create_or_update

    
    """
    parameters = {"properties":{"resourceId":"resourceId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/linkedServices/{linked_service_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', linked_service_name='linked_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_linked_services_delete(client):
    """Test case for linked_services_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/linkedServices/{linked_service_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', linked_service_name='linked_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_linked_services_get(client):
    """Test case for linked_services_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/linkedServices/{linked_service_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', linked_service_name='linked_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_linked_services_list_by_workspace(client):
    """Test case for linked_services_list_by_workspace

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/linkedServices'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

