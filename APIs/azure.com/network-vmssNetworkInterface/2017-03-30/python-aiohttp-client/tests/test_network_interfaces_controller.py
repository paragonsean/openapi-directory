# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.network_interfaces_get_virtual_machine_scale_set_ip_configuration200_response import NetworkInterfacesGetVirtualMachineScaleSetIpConfiguration200Response
from openapi_server.models.network_interfaces_get_virtual_machine_scale_set_network_interface200_response import NetworkInterfacesGetVirtualMachineScaleSetNetworkInterface200Response
from openapi_server.models.network_interfaces_list_virtual_machine_scale_set_ip_configurations200_response import NetworkInterfacesListVirtualMachineScaleSetIpConfigurations200Response
from openapi_server.models.network_interfaces_list_virtual_machine_scale_set_network_interfaces200_response import NetworkInterfacesListVirtualMachineScaleSetNetworkInterfaces200Response


pytestmark = pytest.mark.asyncio

async def test_network_interfaces_get_virtual_machine_scale_set_ip_configuration(client):
    """Test case for network_interfaces_get_virtual_machine_scale_set_ip_configuration

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.Compute/virtualMachineScaleSets/{virtual_machine_scale_set_name}/virtualMachines/{virtualmachine_index}/networkInterfaces/{network_interface_name}/ipConfigurations/{ip_configuration_name}'.format(resource_group_name='resource_group_name_example', virtual_machine_scale_set_name='virtual_machine_scale_set_name_example', virtualmachine_index='virtualmachine_index_example', network_interface_name='network_interface_name_example', ip_configuration_name='ip_configuration_name_example', subscription_id='subscription_id_example'),
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

async def test_network_interfaces_list_virtual_machine_scale_set_ip_configurations(client):
    """Test case for network_interfaces_list_virtual_machine_scale_set_ip_configurations

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.Compute/virtualMachineScaleSets/{virtual_machine_scale_set_name}/virtualMachines/{virtualmachine_index}/networkInterfaces/{network_interface_name}/ipConfigurations'.format(resource_group_name='resource_group_name_example', virtual_machine_scale_set_name='virtual_machine_scale_set_name_example', virtualmachine_index='virtualmachine_index_example', network_interface_name='network_interface_name_example', subscription_id='subscription_id_example'),
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

