# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container_service import ContainerService
from openapi_server.models.container_service_list_result import ContainerServiceListResult


pytestmark = pytest.mark.asyncio

async def test_container_services_create_or_update(client):
    """Test case for container_services_create_or_update

    Creates or updates a container service.
    """
    parameters = {"properties":{"agentPoolProfiles":[{"fqdn":"fqdn","count":8,"name":"name","dnsPrefix":"dnsPrefix","vmSize":"Standard_A0"},{"fqdn":"fqdn","count":8,"name":"name","dnsPrefix":"dnsPrefix","vmSize":"Standard_A0"}],"orchestratorProfile":{"orchestratorType":"Swarm"},"windowsProfile":{"adminUsername":"adminUsername","adminPassword":"adminPassword"},"servicePrincipalProfile":{"clientId":"clientId","secret":"secret"},"diagnosticsProfile":{"vmDiagnostics":{"storageUri":"storageUri","enabled":True}},"customProfile":{"orchestrator":"orchestrator"},"provisioningState":"provisioningState","linuxProfile":{"adminUsername":"adminUsername","ssh":{"publicKeys":[{"keyData":"keyData"},{"keyData":"keyData"}]}},"masterProfile":{"fqdn":"fqdn","count":6,"dnsPrefix":"dnsPrefix"}}}
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

async def test_container_services_list(client):
    """Test case for container_services_list

    Gets a list of container services in the specified subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ContainerService/containerServices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

