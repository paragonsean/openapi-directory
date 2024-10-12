# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aml_compute_nodes_information import AmlComputeNodesInformation
from openapi_server.models.cluster_update_parameters import ClusterUpdateParameters
from openapi_server.models.compute_resource import ComputeResource
from openapi_server.models.compute_secrets import ComputeSecrets
from openapi_server.models.machine_learning_service_error import MachineLearningServiceError
from openapi_server.models.paginated_compute_resources_list import PaginatedComputeResourcesList


pytestmark = pytest.mark.asyncio

async def test_machine_learning_compute_create_or_update_0(client):
    """Test case for machine_learning_compute_create_or_update_0

    
    """
    parameters = {"identity":{"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"name":"name","location":"location","id":"id","type":"type","properties":{"computeLocation":"computeLocation","modifiedOn":"2000-01-23T04:56:07.000+00:00","resourceId":"resourceId","computeType":"AKS","description":"description","provisioningErrors":[{"error":{"code":"code","details":[{"code":"code","message":"message"},{"code":"code","message":"message"}],"message":"message"}},{"error":{"code":"code","details":[{"code":"code","message":"message"},{"code":"code","message":"message"}],"message":"message"}}],"isAttachedCompute":True,"provisioningState":"Unknown","createdOn":"2000-01-23T04:56:07.000+00:00"},"tags":{"key":"tags"}}
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

async def test_machine_learning_compute_delete_0(client):
    """Test case for machine_learning_compute_delete_0

    
    """
    params = [('api-version', 'api_version_example'),
                    ('underlyingResourceAction', 'underlying_resource_action_example')]
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

async def test_machine_learning_compute_get_0(client):
    """Test case for machine_learning_compute_get_0

    
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

async def test_machine_learning_compute_list_by_workspace_0(client):
    """Test case for machine_learning_compute_list_by_workspace_0

    
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

async def test_machine_learning_compute_list_keys_0(client):
    """Test case for machine_learning_compute_list_keys_0

    
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

async def test_machine_learning_compute_list_nodes(client):
    """Test case for machine_learning_compute_list_nodes

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/computes/{compute_name}/listNodes'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', compute_name='compute_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_machine_learning_compute_update_0(client):
    """Test case for machine_learning_compute_update_0

    
    """
    parameters = {"properties":{"scaleSettings":{"minNodeCount":6,"maxNodeCount":0,"nodeIdleTimeBeforeScaleDown":"nodeIdleTimeBeforeScaleDown"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{workspace_name}/computes/{compute_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', compute_name='compute_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

