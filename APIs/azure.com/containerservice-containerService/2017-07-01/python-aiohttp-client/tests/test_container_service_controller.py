# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container_service import ContainerService


pytestmark = pytest.mark.asyncio

async def test_container_services_create_or_update(client):
    """Test case for container_services_create_or_update

    Creates or updates a container service.
    """
    parameters = {"name":"name","location":"location","id":"id","type":"type","properties":{"agentPoolProfiles":[{"fqdn":"fqdn","osDiskSizeGB":616,"storageProfile":"StorageAccount","count":8,"name":"name","osType":"Linux","dnsPrefix":"dnsPrefix","vnetSubnetID":"vnetSubnetID","vmSize":"Standard_A1","ports":[9607,9607]},{"fqdn":"fqdn","osDiskSizeGB":616,"storageProfile":"StorageAccount","count":8,"name":"name","osType":"Linux","dnsPrefix":"dnsPrefix","vnetSubnetID":"vnetSubnetID","vmSize":"Standard_A1","ports":[9607,9607]}],"orchestratorProfile":{"orchestratorType":"Kubernetes","orchestratorVersion":"orchestratorVersion"},"windowsProfile":{"adminUsername":"adminUsername","adminPassword":"adminPassword"},"servicePrincipalProfile":{"clientId":"clientId","keyVaultSecretRef":{"secretName":"secretName","vaultID":"vaultID","version":"version"},"secret":"secret"},"diagnosticsProfile":{"vmDiagnostics":{"storageUri":"storageUri","enabled":True}},"customProfile":{"orchestrator":"orchestrator"},"provisioningState":"provisioningState","linuxProfile":{"adminUsername":"adminUsername","ssh":{"publicKeys":[{"keyData":"keyData"},{"keyData":"keyData"}]}},"masterProfile":{"fqdn":"fqdn","osDiskSizeGB":576,"firstConsecutiveStaticIP":"10.240.255.5","count":5,"dnsPrefix":"dnsPrefix","vnetSubnetID":"vnetSubnetID"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/containerServices/{container_service_name}'.format(resource_group_name='resource_group_name_example', container_service_name='container_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_services_delete(client):
    """Test case for container_services_delete

    Deletes the specified container service.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/containerServices/{container_service_name}'.format(resource_group_name='resource_group_name_example', container_service_name='container_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_container_services_get(client):
    """Test case for container_services_get

    Gets the properties of the specified container service.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/containerServices/{container_service_name}'.format(resource_group_name='resource_group_name_example', container_service_name='container_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

