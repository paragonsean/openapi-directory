# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container_exec_request import ContainerExecRequest
from openapi_server.models.container_exec_response import ContainerExecResponse
from openapi_server.models.container_group import ContainerGroup
from openapi_server.models.container_group_list_result import ContainerGroupListResult
from openapi_server.models.logs import Logs
from openapi_server.models.resource import Resource
from openapi_server.models.usage_list_result import UsageListResult


pytestmark = pytest.mark.asyncio

async def test_container_group_usage_list(client):
    """Test case for container_group_usage_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ContainerInstance/locations/{location}/usages'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_groups_create_or_update(client):
    """Test case for container_groups_create_or_update

    Create or update container groups.
    """
    container_group = {"name":"name","location":"location","id":"id","type":"type","properties":{"instanceView":{"state":"state","events":[{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"},{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"}]},"imageRegistryCredentials":[{"server":"server","password":"password","username":"username"},{"server":"server","password":"password","username":"username"}],"ipAddress":{"dnsNameLabel":"dnsNameLabel","fqdn":"fqdn","ip":"ip","ports":[{"protocol":"TCP","port":3},{"protocol":"TCP","port":3}],"type":"Public"},"osType":"Windows","volumes":[{"azureFile":{"storageAccountName":"storageAccountName","readOnly":True,"storageAccountKey":"storageAccountKey","shareName":"shareName"},"emptyDir":"{}","name":"name","secret":{"key":"secret"},"gitRepo":{"repository":"repository","directory":"directory","revision":"revision"}},{"azureFile":{"storageAccountName":"storageAccountName","readOnly":True,"storageAccountKey":"storageAccountKey","shareName":"shareName"},"emptyDir":"{}","name":"name","secret":{"key":"secret"},"gitRepo":{"repository":"repository","directory":"directory","revision":"revision"}}],"containers":[{"name":"name","properties":{"image":"image","instanceView":{"restartCount":1,"currentState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":0,"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},"events":[{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"},{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"}],"previousState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":0,"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}},"environmentVariables":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"resources":{"requests":{"cpu":7.061401241503109,"memoryInGB":9.301444243932576},"limits":{"cpu":5.637376656633329,"memoryInGB":2.3021358869347655}},"ports":[{"protocol":"TCP","port":5},{"protocol":"TCP","port":5}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True},{"mountPath":"mountPath","name":"name","readOnly":True}]}},{"name":"name","properties":{"image":"image","instanceView":{"restartCount":1,"currentState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":0,"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},"events":[{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"},{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"}],"previousState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":0,"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}},"environmentVariables":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"resources":{"requests":{"cpu":7.061401241503109,"memoryInGB":9.301444243932576},"limits":{"cpu":5.637376656633329,"memoryInGB":2.3021358869347655}},"ports":[{"protocol":"TCP","port":5},{"protocol":"TCP","port":5}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True},{"mountPath":"mountPath","name":"name","readOnly":True}]}}],"provisioningState":"provisioningState","restartPolicy":"Always"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerInstance/containerGroups/{container_group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', container_group_name='container_group_name_example'),
        headers=headers,
        json=container_group,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_groups_delete(client):
    """Test case for container_groups_delete

    Delete the specified container group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerInstance/containerGroups/{container_group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', container_group_name='container_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_groups_get(client):
    """Test case for container_groups_get

    Get the properties of the specified container group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerInstance/containerGroups/{container_group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', container_group_name='container_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_groups_list(client):
    """Test case for container_groups_list

    Get a list of container groups in the specified subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ContainerInstance/containerGroups'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_groups_list_by_resource_group(client):
    """Test case for container_groups_list_by_resource_group

    Get a list of container groups in the specified subscription and resource group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerInstance/containerGroups'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_groups_update(client):
    """Test case for container_groups_update

    Update container groups.
    """
    resource = {"name":"name","location":"location","id":"id","type":"type","tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerInstance/containerGroups/{container_group_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', container_group_name='container_group_name_example'),
        headers=headers,
        json=resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_logs_list(client):
    """Test case for container_logs_list

    Get the logs for a specified container instance.
    """
    params = [('api-version', 'api_version_example'),
                    ('tail', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerInstance/containerGroups/{container_group_name}/containers/{container_name}/logs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', container_group_name='container_group_name_example', container_name='container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_container_launch_exec(client):
    """Test case for start_container_launch_exec

    Starts the exec command for a specific container instance.
    """
    container_exec_request = {"terminalSize":{"column":0,"row":6},"command":"command"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerInstance/containerGroups/{container_group_name}/containers/{container_name}/exec'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', container_group_name='container_group_name_example', container_name='container_name_example'),
        headers=headers,
        json=container_exec_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

