# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.public_ip_addresses_get_virtual_machine_scale_set_public_ip_address200_response import PublicIPAddressesGetVirtualMachineScaleSetPublicIPAddress200Response
from openapi_server.models.public_ip_addresses_list_virtual_machine_scale_set_public_ip_addresses200_response import PublicIPAddressesListVirtualMachineScaleSetPublicIPAddresses200Response


pytestmark = pytest.mark.asyncio

async def test_public_ip_addresses_get_virtual_machine_scale_set_public_ip_address(client):
    """Test case for public_ip_addresses_get_virtual_machine_scale_set_public_ip_address

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtual_machine_scale_set_name}/virtualMachines/{virtualmachine_index}/networkInterfaces/{network_interface_name}/ipconfigurations/{ip_configuration_name}/publicipaddresses/{public_ip_address_name}'.format(resource_group_name='resource_group_name_example', virtual_machine_scale_set_name='virtual_machine_scale_set_name_example', virtualmachine_index='virtualmachine_index_example', network_interface_name='network_interface_name_example', ip_configuration_name='ip_configuration_name_example', public_ip_address_name='public_ip_address_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_addresses_list_virtual_machine_scale_set_public_ip_addresses(client):
    """Test case for public_ip_addresses_list_virtual_machine_scale_set_public_ip_addresses

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtual_machine_scale_set_name}/publicipaddresses'.format(resource_group_name='resource_group_name_example', virtual_machine_scale_set_name='virtual_machine_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_addresses_list_virtual_machine_scale_set_vm_public_ip_addresses(client):
    """Test case for public_ip_addresses_list_virtual_machine_scale_set_vm_public_ip_addresses

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtual_machine_scale_set_name}/virtualMachines/{virtualmachine_index}/networkInterfaces/{network_interface_name}/ipconfigurations/{ip_configuration_name}/publicipaddresses'.format(resource_group_name='resource_group_name_example', virtual_machine_scale_set_name='virtual_machine_scale_set_name_example', virtualmachine_index='virtualmachine_index_example', network_interface_name='network_interface_name_example', ip_configuration_name='ip_configuration_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

