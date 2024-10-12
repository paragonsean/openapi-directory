# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_system_services_updates_available_response import CheckSystemServicesUpdatesAvailableResponse
from openapi_server.models.error_response_wrapper import ErrorResponseWrapper
from openapi_server.models.operationalization_cluster import OperationalizationCluster
from openapi_server.models.operationalization_cluster_credentials import OperationalizationClusterCredentials
from openapi_server.models.operationalization_cluster_update_parameters import OperationalizationClusterUpdateParameters
from openapi_server.models.paginated_operationalization_clusters_list import PaginatedOperationalizationClustersList
from openapi_server.models.update_system_services_response import UpdateSystemServicesResponse


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_check_system_services_updates_available(client):
    """Test case for operationalization_clusters_check_system_services_updates_available

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{cluster_name}/checkSystemServicesUpdatesAvailable'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operationalization_clusters_create_or_update(client):
    """Test case for operationalization_clusters_create_or_update

    
    """
    parameters = {"properties":{"clusterType":"ACS","containerService":{"clusterFqdn":"clusterFqdn","orchestratorType":"Kubernetes","masterCount":3,"systemServices":[{"publicIpAddress":"publicIpAddress","version":"version","systemServiceType":"None"},{"publicIpAddress":"publicIpAddress","version":"version","systemServiceType":"None"}],"orchestratorProperties":{"servicePrincipal":{"clientId":"clientId","secret":"secret"}},"agentCount":8,"agentVmSize":"Standard_D3_v2"},"modifiedOn":"2000-01-23T04:56:07.000+00:00","globalServiceConfiguration":{"etag":"etag","serviceAuth":{"secondaryAuthKeyHash":"secondaryAuthKeyHash","primaryAuthKeyHash":"primaryAuthKeyHash"},"ssl":{"cname":"cname","cert":"cert","key":"key","status":"Enabled"},"autoScale":{"maxReplicas":1,"targetUtilization":2.3021358869347655,"minReplicas":1,"refreshPeriodInSeconds":5,"status":"Disabled"}},"containerRegistry":{"resourceId":"resourceId"},"description":"description","provisioningErrors":[{"error":{"code":"code","details":[{"code":"code","message":"message"},{"code":"code","message":"message"}],"message":"message"}},{"error":{"code":"code","details":[{"code":"code","message":"message"},{"code":"code","message":"message"}],"message":"message"}}],"provisioningState":"Unknown","storageAccount":{"resourceId":"resourceId"},"createdOn":"2000-01-23T04:56:07.000+00:00","appInsights":{"resourceId":"resourceId"}}}
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
    params = [('api-version', 'api_version_example'),
                    ('deleteAll', True)]
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

async def test_operationalization_clusters_update_system_services(client):
    """Test case for operationalization_clusters_update_system_services

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearningCompute/operationalizationClusters/{cluster_name}/updateSystemServices'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

