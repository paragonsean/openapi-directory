# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_update_response import CheckUpdateResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operationalization_cluster import OperationalizationCluster
from openapi_server.models.operationalization_cluster_credentials import OperationalizationClusterCredentials
from openapi_server.models.operationalization_cluster_update_parameters import OperationalizationClusterUpdateParameters
from openapi_server.models.paginated_operationalization_clusters_list import PaginatedOperationalizationClustersList
from openapi_server.models.update_system_response import UpdateSystemResponse


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_check_update(client):
    """Test case for operationalization_clusters_check_update

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{cluster_name}/checkUpdate'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_create_or_update(client):
    """Test case for operationalization_clusters_create_or_update

    
    """
    parameters = {"properties":{"clusterType":"ACS","containerService":{"clusterFqdn":"clusterFqdn","orchestratorType":"Kubernetes","systemServices":["Scoring","Scoring"],"orchestratorProperties":{"servicePrincipal":{"clientId":"clientId","secret":"secret"}},"agentCount":8,"agentVmSize":"Standard_D2_v2"},"modifiedOn":"2000-01-23T04:56:07.000+00:00","globalServiceConfiguration":{"etag":"etag","serviceAuth":{"secondaryAuthKeyHash":"secondaryAuthKeyHash","primaryAuthKeyHash":"primaryAuthKeyHash"},"ssl":{"cert":"cert","key":"key","status":"Enabled"},"autoScale":{"maxReplicas":1,"targetUtilization":5.637376656633329,"minReplicas":1,"refreshPeriodInSeconds":5,"status":"Disabled"}},"containerRegistry":{"resourceId":"resourceId"},"description":"description","provisioningState":"Unknown","storageAccount":{"resourceId":"resourceId"},"createdOn":"2000-01-23T04:56:07.000+00:00","appInsights":{"apiKey":"apiKey","appId":"appId"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{cluster_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_delete(client):
    """Test case for operationalization_clusters_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{cluster_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_get(client):
    """Test case for operationalization_clusters_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{cluster_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_list_by_resource_group(client):
    """Test case for operationalization_clusters_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningCompute/operationalizationClusters'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_list_by_subscription_id(client):
    """Test case for operationalization_clusters_list_by_subscription_id

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MachineLearningCompute/operationalizationClusters'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_list_keys(client):
    """Test case for operationalization_clusters_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{cluster_name}/listKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_update(client):
    """Test case for operationalization_clusters_update

    
    """
    parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{cluster_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_update_system(client):
    """Test case for operationalization_clusters_update_system

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{cluster_name}/updateSystem'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

