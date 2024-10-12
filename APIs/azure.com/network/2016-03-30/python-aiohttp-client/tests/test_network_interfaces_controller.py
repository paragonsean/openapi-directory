# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.network_interface import NetworkInterface
from openapi_server.models.network_interface_list_result import NetworkInterfaceListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_interfaces_create_or_update(client):
    """Test case for network_interfaces_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"ipConfigurations":[null,null],"virtualMachine":{"id":"id"},"macAddress":"macAddress","dnsSettings":{"appliedDnsServers":["appliedDnsServers","appliedDnsServers"],"internalDnsNameLabel":"internalDnsNameLabel","internalDomainNameSuffix":"internalDomainNameSuffix","internalFqdn":"internalFqdn","dnsServers":["dnsServers","dnsServers"]},"resourceGuid":"resourceGuid","provisioningState":"provisioningState","enableIPForwarding":True,"primary":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkInterfaces/{network_interface_name}'.format(resource_group_name='resource_group_name_example', network_interface_name='network_interface_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_interfaces_delete(client):
    """Test case for network_interfaces_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkInterfaces/{network_interface_name}'.format(resource_group_name='resource_group_name_example', network_interface_name='network_interface_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_interfaces_get(client):
    """Test case for network_interfaces_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkInterfaces/{network_interface_name}'.format(resource_group_name='resource_group_name_example', network_interface_name='network_interface_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_interfaces_get_virtual_machine_scale_set_network_interface(client):
    """Test case for network_interfaces_get_virtual_machine_scale_set_network_interface

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.Compute/virtualMachineScaleSets/{virtual_machine_scale_set_name}/virtualMachines/{virtualmachine_index}/networkInterfaces/{network_interface_name}'.format(resource_group_name='resource_group_name_example', virtual_machine_scale_set_name='virtual_machine_scale_set_name_example', virtualmachine_index='virtualmachine_index_example', network_interface_name='network_interface_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_interfaces_list(client):
    """Test case for network_interfaces_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkInterfaces'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_interfaces_list_all(client):
    """Test case for network_interfaces_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/networkInterfaces'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_interfaces_list_virtual_machine_scale_set_network_interfaces(client):
    """Test case for network_interfaces_list_virtual_machine_scale_set_network_interfaces

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.Compute/virtualMachineScaleSets/{virtual_machine_scale_set_name}/networkInterfaces'.format(resource_group_name='resource_group_name_example', virtual_machine_scale_set_name='virtual_machine_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_interfaces_list_virtual_machine_scale_set_vm_network_interfaces(client):
    """Test case for network_interfaces_list_virtual_machine_scale_set_vm_network_interfaces

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.Compute/virtualMachineScaleSets/{virtual_machine_scale_set_name}/virtualMachines/{virtualmachine_index}/networkInterfaces'.format(resource_group_name='resource_group_name_example', virtual_machine_scale_set_name='virtual_machine_scale_set_name_example', virtualmachine_index='virtualmachine_index_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

