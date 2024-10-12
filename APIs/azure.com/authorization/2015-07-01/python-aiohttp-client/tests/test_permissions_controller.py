# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.permission_get_result import PermissionGetResult


pytestmark = pytest.mark.asyncio

async def test_permissions_list_for_resource(client):
    """Test case for permissions_list_for_resource

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/{resource_provider_namespace}/{parent_resource_path}/{resource_type}/{resource_name}/providers/Microsoft.Authorization/permissions'.format(resource_group_name='resource_group_name_example', resource_provider_namespace='resource_provider_namespace_example', parent_resource_path='parent_resource_path_example', resource_type='resource_type_example', resource_name='resource_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permissions_list_for_resource_group(client):
    """Test case for permissions_list_for_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Authorization/permissions'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

