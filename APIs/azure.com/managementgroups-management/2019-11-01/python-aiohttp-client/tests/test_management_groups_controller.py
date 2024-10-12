# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_management_group_request import CreateManagementGroupRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.management_group import ManagementGroup
from openapi_server.models.management_group_list_result import ManagementGroupListResult
from openapi_server.models.operation_results import OperationResults
from openapi_server.models.patch_management_group_request import PatchManagementGroupRequest


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
    create_management_group_request = {"name":"name","id":"id","type":"type","properties":{"children":[{"children":[null,null],"displayName":"displayName","roles":["roles","roles"],"name":"name","id":"id","type":"Microsoft.Management/managementGroups"},{"children":[null,null],"displayName":"displayName","roles":["roles","roles"],"name":"name","id":"id","type":"Microsoft.Management/managementGroups"}],"displayName":"displayName","roles":["roles","roles"],"tenantId":"tenantId","details":{"parent":{"displayName":"displayName","name":"name","id":"id"},"updatedTime":"2000-01-23T04:56:07.000+00:00","updatedBy":"updatedBy","version":0.8008281904610115}}}
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
                    ('$recurse', True),
                    ('$filter', 'filter_example')]
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
    patch_group_request = {"displayName":"displayName","parentId":"parentId"}
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
        json=patch_group_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

