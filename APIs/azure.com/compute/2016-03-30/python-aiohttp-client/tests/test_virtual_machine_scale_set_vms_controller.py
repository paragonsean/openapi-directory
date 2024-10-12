# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.virtual_machine_scale_set_vm import VirtualMachineScaleSetVM
from openapi_server.models.virtual_machine_scale_set_vm_instance_view import VirtualMachineScaleSetVMInstanceView
from openapi_server.models.virtual_machine_scale_set_vm_list_result import VirtualMachineScaleSetVMListResult


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_deallocate(client):
    """Test case for virtual_machine_scale_set_vms_deallocate

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/deallocate'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_delete(client):
    """Test case for virtual_machine_scale_set_vms_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_get(client):
    """Test case for virtual_machine_scale_set_vms_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_get_instance_view(client):
    """Test case for virtual_machine_scale_set_vms_get_instance_view

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/instanceView'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_list(client):
    """Test case for virtual_machine_scale_set_vms_list

    
    """
    params = [('$filter', 'filter_example'),
                    ('$select', 'select_example'),
                    ('$expand', 'expand_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtual_machine_scale_set_name}/virtualMachines'.format(resource_group_name='resource_group_name_example', virtual_machine_scale_set_name='virtual_machine_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_power_off(client):
    """Test case for virtual_machine_scale_set_vms_power_off

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/poweroff'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_reimage(client):
    """Test case for virtual_machine_scale_set_vms_reimage

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/reimage'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_restart(client):
    """Test case for virtual_machine_scale_set_vms_restart

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/restart'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_vms_start(client):
    """Test case for virtual_machine_scale_set_vms_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/virtualmachines/{instance_id}/start'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', instance_id='instance_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

