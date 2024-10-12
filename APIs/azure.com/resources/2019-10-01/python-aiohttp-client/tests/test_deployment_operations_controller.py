# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.deployment_operation import DeploymentOperation
from openapi_server.models.deployment_operations_list_result import DeploymentOperationsListResult


pytestmark = pytest.mark.asyncio

async def test_deployment_operations_get(client):
    """Test case for deployment_operations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/deployments/{deployment_name}/operations/{operation_id}'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_operations_get_at_management_group_scope(client):
    """Test case for deployment_operations_get_at_management_group_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/providers/Microsoft.Resources/deployments/{deployment_name}/operations/{operation_id}'.format(group_id='group_id_example', deployment_name='deployment_name_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_operations_get_at_scope(client):
    """Test case for deployment_operations_get_at_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Resources/deployments/{deployment_name}/operations/{operation_id}'.format(scope='scope_example', deployment_name='deployment_name_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_operations_get_at_subscription_scope(client):
    """Test case for deployment_operations_get_at_subscription_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments/{deployment_name}/operations/{operation_id}'.format(deployment_name='deployment_name_example', operation_id='operation_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_operations_get_at_tenant_scope(client):
    """Test case for deployment_operations_get_at_tenant_scope

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Resources/deployments/{deployment_name}/operations/{operation_id}'.format(deployment_name='deployment_name_example', operation_id='operation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_operations_list(client):
    """Test case for deployment_operations_list

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/deployments/{deployment_name}/operations'.format(resource_group_name='resource_group_name_example', deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_operations_list_at_management_group_scope(client):
    """Test case for deployment_operations_list_at_management_group_scope

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Management/managementGroups/{group_id}/providers/Microsoft.Resources/deployments/{deployment_name}/operations'.format(group_id='group_id_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_operations_list_at_scope(client):
    """Test case for deployment_operations_list_at_scope

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{scope}/providers/Microsoft.Resources/deployments/{deployment_name}/operations'.format(scope='scope_example', deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_operations_list_at_subscription_scope(client):
    """Test case for deployment_operations_list_at_subscription_scope

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Resources/deployments/{deployment_name}/operations'.format(deployment_name='deployment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployment_operations_list_at_tenant_scope(client):
    """Test case for deployment_operations_list_at_tenant_scope

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Resources/deployments/{deployment_name}/operations'.format(deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

