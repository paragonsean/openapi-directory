# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cached_images_list_result import CachedImagesListResult
from openapi_server.models.capabilities_list_result import CapabilitiesListResult
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.container_exec_request import ContainerExecRequest
from openapi_server.models.container_exec_response import ContainerExecResponse
from openapi_server.models.container_group import ContainerGroup
from openapi_server.models.container_group_list_result import ContainerGroupListResult
from openapi_server.models.logs import Logs
from openapi_server.models.resource import Resource
from openapi_server.models.usage_list_result import UsageListResult


pytestmark = pytest.mark.asyncio

async def test_container_execute_command(client):
    """Test case for container_execute_command

    Executes a command in a specific container instance.
    """
    container_exec_request = {"terminalSize":{"rows":6,"cols":0},"command":"command"}
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
    container_group = {"identity":{"userAssignedIdentities":{"key":{"clientId":"clientId","principalId":"principalId"}},"tenantId":"tenantId","principalId":"principalId","type":"SystemAssigned"},"name":"name","location":"location","id":"id","type":"type","properties":{"diagnostics":{"logAnalytics":{"logType":"ContainerInsights","metadata":{"key":"metadata"},"workspaceId":"workspaceId","workspaceKey":"workspaceKey"}},"instanceView":{"state":"state","events":[{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"},{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"}]},"dnsConfig":{"options":"options","searchDomains":"searchDomains","nameServers":["nameServers","nameServers"]},"imageRegistryCredentials":[{"server":"server","password":"password","username":"username"},{"server":"server","password":"password","username":"username"}],"ipAddress":{"dnsNameLabel":"dnsNameLabel","fqdn":"fqdn","ip":"ip","ports":[{"protocol":"TCP","port":6},{"protocol":"TCP","port":6}],"type":"Public"},"osType":"Windows","volumes":[{"azureFile":{"storageAccountName":"storageAccountName","readOnly":True,"storageAccountKey":"storageAccountKey","shareName":"shareName"},"emptyDir":"{}","name":"name","secret":{"key":"secret"},"gitRepo":{"repository":"repository","directory":"directory","revision":"revision"}},{"azureFile":{"storageAccountName":"storageAccountName","readOnly":True,"storageAccountKey":"storageAccountKey","shareName":"shareName"},"emptyDir":"{}","name":"name","secret":{"key":"secret"},"gitRepo":{"repository":"repository","directory":"directory","revision":"revision"}}],"networkProfile":{"id":"id"},"containers":[{"name":"name","properties":{"image":"image","livenessProbe":{"failureThreshold":5,"periodSeconds":7,"timeoutSeconds":3,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"httpGet":{"path":"path","scheme":"http","port":5}},"instanceView":{"restartCount":1,"currentState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":0,"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},"events":[{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"},{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"}],"previousState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":0,"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}},"environmentVariables":[{"secureValue":"secureValue","name":"name","value":"value"},{"secureValue":"secureValue","name":"name","value":"value"}],"readinessProbe":{"failureThreshold":5,"periodSeconds":7,"timeoutSeconds":3,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"httpGet":{"path":"path","scheme":"http","port":5}},"resources":{"requests":{"cpu":1.0246457001441578,"memoryInGB":1.4894159098541704,"gpu":{"count":7,"sku":"K80"}},"limits":{"cpu":4.145608029883936,"memoryInGB":1.2315135367772556,"gpu":{"count":7,"sku":"K80"}}},"ports":[{"protocol":"TCP","port":2},{"protocol":"TCP","port":2}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True},{"mountPath":"mountPath","name":"name","readOnly":True}]}},{"name":"name","properties":{"image":"image","livenessProbe":{"failureThreshold":5,"periodSeconds":7,"timeoutSeconds":3,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"httpGet":{"path":"path","scheme":"http","port":5}},"instanceView":{"restartCount":1,"currentState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":0,"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},"events":[{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"},{"firstTimestamp":"2000-01-23T04:56:07.000+00:00","lastTimestamp":"2000-01-23T04:56:07.000+00:00","count":6,"name":"name","message":"message","type":"type"}],"previousState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":0,"startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}},"environmentVariables":[{"secureValue":"secureValue","name":"name","value":"value"},{"secureValue":"secureValue","name":"name","value":"value"}],"readinessProbe":{"failureThreshold":5,"periodSeconds":7,"timeoutSeconds":3,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"httpGet":{"path":"path","scheme":"http","port":5}},"resources":{"requests":{"cpu":1.0246457001441578,"memoryInGB":1.4894159098541704,"gpu":{"count":7,"sku":"K80"}},"limits":{"cpu":4.145608029883936,"memoryInGB":1.2315135367772556,"gpu":{"count":7,"sku":"K80"}}},"ports":[{"protocol":"TCP","port":2},{"protocol":"TCP","port":2}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True},{"mountPath":"mountPath","name":"name","readOnly":True}]}}],"provisioningState":"provisioningState","restartPolicy":"Always"},"tags":{"key":"tags"}}
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

async def test_container_groups_restart(client):
    """Test case for container_groups_restart

    Restarts all containers in a container group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerInstance/containerGroups/{container_group_name}/restart'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', container_group_name='container_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_groups_start(client):
    """Test case for container_groups_start

    Starts all containers in a container group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerInstance/containerGroups/{container_group_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', container_group_name='container_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_groups_stop(client):
    """Test case for container_groups_stop

    Stops all containers in a container group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerInstance/containerGroups/{container_group_name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', container_group_name='container_group_name_example'),
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

async def test_container_list_logs(client):
    """Test case for container_list_logs

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

async def test_list_cached_images(client):
    """Test case for list_cached_images

    Get the list of cached images.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ContainerInstance/locations/{location}/cachedImages'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_capabilities(client):
    """Test case for list_capabilities

    Get the list of capabilities of the location.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ContainerInstance/locations/{location}/capabilities'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_association_link_delete(client):
    """Test case for service_association_link_delete

    Delete the container instance service association link for the subnet.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{virtual_network_name}/subnets/{subnet_name}/providers/Microsoft.ContainerInstance/serviceAssociationLinks/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', subnet_name='subnet_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

