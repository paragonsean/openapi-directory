# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_result import CheckNameResult
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_check_name_request import ClusterCheckNameRequest
from openapi_server.models.cluster_list_result import ClusterListResult
from openapi_server.models.cluster_update import ClusterUpdate
from openapi_server.models.list_resource_skus_result import ListResourceSkusResult


pytestmark = pytest.mark.asyncio

async def test_clusters_check_name_availability(client):
    """Test case for clusters_check_name_availability

    
    """
    cluster_name = {"name":"name","type":"Microsoft.Kusto/clusters"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Kusto/locations/{location}/checkNameAvailability'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=cluster_name,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_create_or_update(client):
    """Test case for clusters_create_or_update

    
    """
    parameters = {"sku":{"tier":"Basic","name":"Standard_DS13_v2+1TB_PS","capacity":5},"zones":["zones","zones"],"properties":{"dataIngestionUri":"dataIngestionUri","trustedExternalTenants":[{"value":"value"},{"value":"value"}],"optimizedAutoscale":{"isEnabled":True,"maximum":0,"minimum":6,"version":1},"enableStreamingIngest":False,"enableDiskEncryption":True,"virtualNetworkConfiguration":{"subnetId":"subnetId","enginePublicIpId":"enginePublicIpId","dataManagementPublicIpId":"dataManagementPublicIpId"},"provisioningState":"Running","state":"Creating","uri":"uri"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_delete(client):
    """Test case for clusters_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_get(client):
    """Test case for clusters_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_list(client):
    """Test case for clusters_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Kusto/clusters'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_list_by_resource_group(client):
    """Test case for clusters_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_list_skus_by_resource(client):
    """Test case for clusters_list_skus_by_resource

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/skus'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_start(client):
    """Test case for clusters_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/start'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_stop(client):
    """Test case for clusters_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/stop'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_update(client):
    """Test case for clusters_update

    
    """
    parameters = {"location":"location","sku":{"tier":"Basic","name":"Standard_DS13_v2+1TB_PS","capacity":5},"properties":{"dataIngestionUri":"dataIngestionUri","trustedExternalTenants":[{"value":"value"},{"value":"value"}],"optimizedAutoscale":{"isEnabled":True,"maximum":0,"minimum":6,"version":1},"enableStreamingIngest":False,"enableDiskEncryption":True,"virtualNetworkConfiguration":{"subnetId":"subnetId","enginePublicIpId":"enginePublicIpId","dataManagementPublicIpId":"dataManagementPublicIpId"},"provisioningState":"Running","state":"Creating","uri":"uri"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

