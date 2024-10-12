# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_list_result import ApplicationListResult
from openapi_server.models.applications_list_by_cluster_default_response import ApplicationsListByClusterDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_applications_create(client):
    """Test case for applications_create

    
    """
    parameters = {"etag":"etag","properties":{"httpsEndpoints":[{"destinationPort":3,"disableGatewayAuth":True,"publicPort":2,"location":"location","accessModes":["accessModes","accessModes"],"subDomainSuffix":"subDomainSuffix"},{"destinationPort":3,"disableGatewayAuth":True,"publicPort":2,"location":"location","accessModes":["accessModes","accessModes"],"subDomainSuffix":"subDomainSuffix"}],"marketplaceIdentifier":"marketplaceIdentifier","applicationType":"applicationType","installScriptActions":[{"roles":["roles","roles"],"name":"name","parameters":"parameters","uri":"uri","applicationName":"applicationName"},{"roles":["roles","roles"],"name":"name","parameters":"parameters","uri":"uri","applicationName":"applicationName"}],"applicationState":"applicationState","createdDate":"createdDate","computeProfile":{"roles":[{"targetInstanceCount":9,"hardwareProfile":{"vmSize":"vmSize"},"scriptActions":[{"name":"name","parameters":"parameters","uri":"uri"},{"name":"name","parameters":"parameters","uri":"uri"}],"dataDisksGroups":[{"disksPerNode":2,"storageAccountType":"storageAccountType","diskSizeGB":5},{"disksPerNode":2,"storageAccountType":"storageAccountType","diskSizeGB":5}],"name":"name","minInstanceCount":7,"virtualNetworkProfile":{"subnet":"subnet","id":"id"},"autoscale":{"recurrence":{"schedule":[{"days":["Monday","Monday"],"timeAndCapacity":{"maxInstanceCount":1,"minInstanceCount":5,"time":"time"}},{"days":["Monday","Monday"],"timeAndCapacity":{"maxInstanceCount":1,"minInstanceCount":5,"time":"time"}}],"timeZone":"timeZone"},"capacity":{"maxInstanceCount":0,"minInstanceCount":6}},"osProfile":{"linuxOperatingSystemProfile":{"password":"password","sshProfile":{"publicKeys":[{"certificateData":"certificateData"},{"certificateData":"certificateData"}]},"username":"username"}}},{"targetInstanceCount":9,"hardwareProfile":{"vmSize":"vmSize"},"scriptActions":[{"name":"name","parameters":"parameters","uri":"uri"},{"name":"name","parameters":"parameters","uri":"uri"}],"dataDisksGroups":[{"disksPerNode":2,"storageAccountType":"storageAccountType","diskSizeGB":5},{"disksPerNode":2,"storageAccountType":"storageAccountType","diskSizeGB":5}],"name":"name","minInstanceCount":7,"virtualNetworkProfile":{"subnet":"subnet","id":"id"},"autoscale":{"recurrence":{"schedule":[{"days":["Monday","Monday"],"timeAndCapacity":{"maxInstanceCount":1,"minInstanceCount":5,"time":"time"}},{"days":["Monday","Monday"],"timeAndCapacity":{"maxInstanceCount":1,"minInstanceCount":5,"time":"time"}}],"timeZone":"timeZone"},"capacity":{"maxInstanceCount":0,"minInstanceCount":6}},"osProfile":{"linuxOperatingSystemProfile":{"password":"password","sshProfile":{"publicKeys":[{"certificateData":"certificateData"},{"certificateData":"certificateData"}]},"username":"username"}}}]},"sshEndpoints":[{"destinationPort":4,"publicPort":7,"location":"location"},{"destinationPort":4,"publicPort":7,"location":"location"}],"provisioningState":"provisioningState","uninstallScriptActions":[{"roles":["roles","roles"],"name":"name","parameters":"parameters","uri":"uri","applicationName":"applicationName"},{"roles":["roles","roles"],"name":"name","parameters":"parameters","uri":"uri","applicationName":"applicationName"}],"errors":[{"code":"code","message":"message"},{"code":"code","message":"message"}]},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/applications/{application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_delete(client):
    """Test case for applications_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/applications/{application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_get(client):
    """Test case for applications_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/applications/{application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_list_by_cluster(client):
    """Test case for applications_list_by_cluster

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.HDInsight/clusters/{cluster_name}/applications'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', cluster_name='cluster_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

