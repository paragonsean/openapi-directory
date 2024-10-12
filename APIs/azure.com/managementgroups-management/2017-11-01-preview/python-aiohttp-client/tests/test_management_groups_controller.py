# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_management_group_request import CreateManagementGroupRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.management_group import ManagementGroup
from openapi_server.models.management_group_list_result import ManagementGroupListResult


pytestmark = pytest.mark.asyncio

async def test_management_group_subscriptions_create(client):
    """Test case for management_group_subscriptions_create

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'cache_control': 'no-cache',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/subscriptions/{subscription_id}'.format(group_id='group_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_group_subscriptions_delete(client):
    """Test case for management_group_subscriptions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'cache_control': 'no-cache',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/subscriptions/{subscription_id}'.format(group_id='group_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_groups_create_or_update(client):
    """Test case for management_groups_create_or_update

    
    """
    create_management_group_request = {"displayName":"displayName","parentId":"parentId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cache_control': 'no-cache',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/Microsoft.Management/managementGroups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        json=create_management_group_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_groups_delete(client):
    """Test case for management_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'cache_control': 'no-cache',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/Microsoft.Management/managementGroups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_groups_get(client):
    """Test case for management_groups_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example'),
                    ('$recurse', True)]
    headers = { 
        'Accept': 'application/json',
        'cache_control': 'no-cache',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_groups_list(client):
    """Test case for management_groups_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
        'cache_control': 'no-cache',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_management_groups_update(client):
    """Test case for management_groups_update

    
    """
    create_management_group_request = {"displayName":"displayName","parentId":"parentId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cache_control': 'no-cache',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Management/managementGroups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        json=create_management_group_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

