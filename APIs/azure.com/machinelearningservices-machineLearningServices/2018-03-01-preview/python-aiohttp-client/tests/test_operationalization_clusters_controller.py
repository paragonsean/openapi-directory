# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.compute_resource import ComputeResource
from openapi_server.models.compute_secrets import ComputeSecrets
from openapi_server.models.machine_learning_service_error import MachineLearningServiceError
from openapi_server.models.paginated_compute_resources_list import PaginatedComputeResourcesList


pytestmark = pytest.mark.asyncio

async def test_machine_learning_compute_create_or_update(client):
    """Test case for machine_learning_compute_create_or_update

    
    """
    parameters = {"identity":{"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"name":"name","location":"location","id":"id","type":"type","properties":{"computeLocation":"computeLocation","modifiedOn":"2000-01-23T04:56:07.000+00:00","resourceId":"resourceId","computeType":"AKS","description":"description","provisioningErrors":[{"error":{"code":"code","details":[{"code":"code","message":"message"},{"code":"code","message":"message"}],"message":"message"}},{"error":{"code":"code","details":[{"code":"code","message":"message"},{"code":"code","message":"message"}],"message":"message"}}],"provisioningState":"Unknown","createdOn":"2000-01-23T04:56:07.000+00:00"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/computes/{compute_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', compute_name='compute_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_machine_learning_compute_delete(client):
    """Test case for machine_learning_compute_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/computes/{compute_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', compute_name='compute_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_machine_learning_compute_get(client):
    """Test case for machine_learning_compute_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/computes/{compute_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', compute_name='compute_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_machine_learning_compute_list_by_workspace(client):
    """Test case for machine_learning_compute_list_by_workspace

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/computes'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_machine_learning_compute_list_keys(client):
    """Test case for machine_learning_compute_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/computes/{compute_name}/listKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', compute_name='compute_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_machine_learning_compute_system_update(client):
    """Test case for machine_learning_compute_system_update

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/computes/{compute_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', compute_name='compute_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

