# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_create_parameters_extended import ClusterCreateParametersExtended
from openapi_server.models.cluster_disk_encryption_parameters import ClusterDiskEncryptionParameters
from openapi_server.models.cluster_list_result import ClusterListResult
from openapi_server.models.cluster_patch_parameters import ClusterPatchParameters
from openapi_server.models.cluster_resize_parameters import ClusterResizeParameters
from openapi_server.models.clusters_list_default_response import ClustersListDefaultResponse
from openapi_server.models.gateway_settings import GatewaySettings
from openapi_server.models.update_gateway_settings_parameters import UpdateGatewaySettingsParameters


pytestmark = pytest.mark.asyncio

async def test_clusters_create(client):
    """Test case for clusters_create

    
    """
    parameters = {"identity":{"userAssignedIdentities":{"key":{"clientId":"clientId","principalId":"principalId"}},"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"location":"location","properties":{"diskEncryptionProperties":{"keyVersion":"keyVersion","keyName":"keyName","vaultUri":"vaultUri","encryptionAlgorithm":"RSA-OAEP","msiResourceId":"msiResourceId"},"tier":"Standard","computeProfile":{"roles":[{"targetInstanceCount":9,"hardwareProfile":{"vmSize":"vmSize"},"scriptActions":[{"name":"name","parameters":"parameters","uri":"uri"},{"name":"name","parameters":"parameters","uri":"uri"}],"dataDisksGroups":[{"disksPerNode":2,"storageAccountType":"storageAccountType","diskSizeGB":5},{"disksPerNode":2,"storageAccountType":"storageAccountType","diskSizeGB":5}],"name":"name","minInstanceCount":7,"virtualNetworkProfile":{"subnet":"subnet","id":"id"},"autoscale":{"recurrence":{"schedule":[{"days":["Monday","Monday"],"timeAndCapacity":{"maxInstanceCount":1,"minInstanceCount":5,"time":"time"}},{"days":["Monday","Monday"],"timeAndCapacity":{"maxInstanceCount":1,"minInstanceCount":5,"time":"time"}}],"timeZone":"timeZone"},"capacity":{"maxInstanceCount":0,"minInstanceCount":6}},"osProfile":{"linuxOperatingSystemProfile":{"password":"password","sshProfile":{"publicKeys":[{"certificateData":"certificateData"},{"certificateData":"certificateData"}]},"username":"username"}}},{"targetInstanceCount":9,"hardwareProfile":{"vmSize":"vmSize"},"scriptActions":[{"name":"name","parameters":"parameters","uri":"uri"},{"name":"name","parameters":"parameters","uri":"uri"}],"dataDisksGroups":[{"disksPerNode":2,"storageAccountType":"storageAccountType","diskSizeGB":5},{"disksPerNode":2,"storageAccountType":"storageAccountType","diskSizeGB":5}],"name":"name","minInstanceCount":7,"virtualNetworkProfile":{"subnet":"subnet","id":"id"},"autoscale":{"recurrence":{"schedule":[{"days":["Monday","Monday"],"timeAndCapacity":{"maxInstanceCount":1,"minInstanceCount":5,"time":"time"}},{"days":["Monday","Monday"],"timeAndCapacity":{"maxInstanceCount":1,"minInstanceCount":5,"time":"time"}}],"timeZone":"timeZone"},"capacity":{"maxInstanceCount":0,"minInstanceCount":6}},"osProfile":{"linuxOperatingSystemProfile":{"password":"password","sshProfile":{"publicKeys":[{"certificateData":"certificateData"},{"certificateData":"certificateData"}]},"username":"username"}}}]},"securityProfile":{"domainUsername":"domainUsername","aaddsResourceId":"aaddsResourceId","organizationalUnitDN":"organizationalUnitDN","domain":"domain","clusterUsersGroupDNs":["clusterUsersGroupDNs","clusterUsersGroupDNs"],"domainUserPassword":"domainUserPassword","ldapsUrls":["ldapsUrls","ldapsUrls"],"msiResourceId":"msiResourceId","directoryType":"ActiveDirectory"},"clusterDefinition":{"blueprint":"blueprint","configurations":"{}","kind":"kind","componentVersion":{"key":"componentVersion"}},"storageProfile":{"storageaccounts":[{"container":"container","fileSystem":"fileSystem","isDefault":True,"resourceId":"resourceId","name":"name","msiResourceId":"msiResourceId","key":"key"},{"container":"container","fileSystem":"fileSystem","isDefault":True,"resourceId":"resourceId","name":"name","msiResourceId":"msiResourceId","key":"key"}]},"osType":"Windows","clusterVersion":"clusterVersion","kafkaRestProperties":{"clientGroupInfo":{"groupName":"groupName","groupId":"groupId"}}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
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
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
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
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_get_gateway_settings(client):
    """Test case for clusters_get_gateway_settings

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/getGatewaySettings'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
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
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.HDInsight/clusters'.format(subscription_id='subscription_id_example'),
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
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_resize(client):
    """Test case for clusters_resize

    
    """
    parameters = {"targetInstanceCount":0}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/roles/{role_name}/resize'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', role_name='role_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_rotate_disk_encryption_key(client):
    """Test case for clusters_rotate_disk_encryption_key

    
    """
    parameters = {"keyVersion":"keyVersion","keyName":"keyName","vaultUri":"vaultUri"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/rotatediskencryptionkey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_update(client):
    """Test case for clusters_update

    
    """
    parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clusters_update_gateway_settings(client):
    """Test case for clusters_update_gateway_settings

    
    """
    parameters = {"restAuthCredential.username":"restAuthCredential.username","restAuthCredential.password":"restAuthCredential.password","restAuthCredential.isEnabled":True}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/updateGatewaySettings'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

