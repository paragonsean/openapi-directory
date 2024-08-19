# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.virtual_machine_scale_set_extension import VirtualMachineScaleSetExtension
from openapi_server.models.virtual_machine_scale_set_extension_list_result import VirtualMachineScaleSetExtensionListResult


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_extensions_create_or_update(client):
    """Test case for virtual_machine_scale_set_extensions_create_or_update

    
    """
    extension_parameters = {"name":"name","properties":{"settings":"{}","autoUpgradeMinorVersion":True,"publisher":"publisher","provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/extensions/{vmss_extension_name}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', vmss_extension_name='vmss_extension_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=extension_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_extensions_delete(client):
    """Test case for virtual_machine_scale_set_extensions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/extensions/{vmss_extension_name}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', vmss_extension_name='vmss_extension_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_extensions_get(client):
    """Test case for virtual_machine_scale_set_extensions_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/extensions/{vmss_extension_name}'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', vmss_extension_name='vmss_extension_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_extensions_list(client):
    """Test case for virtual_machine_scale_set_extensions_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/extensions'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

