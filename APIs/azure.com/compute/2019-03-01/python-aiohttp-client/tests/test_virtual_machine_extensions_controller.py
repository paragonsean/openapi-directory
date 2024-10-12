# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_machine_extension import VirtualMachineExtension
from openapi_server.models.virtual_machine_extension_update import VirtualMachineExtensionUpdate
from openapi_server.models.virtual_machine_extensions_list_result import VirtualMachineExtensionsListResult


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_extensions_create_or_update(client):
    """Test case for virtual_machine_extensions_create_or_update

    
    """
    extension_parameters = {"properties":{"settings":"{}","instanceView":{"name":"name","statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"substatuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"type":"type","typeHandlerVersion":"typeHandlerVersion"},"autoUpgradeMinorVersion":True,"publisher":"publisher","provisioningState":"provisioningState","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/extensions/{vm_extension_name}'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', vm_extension_name='vm_extension_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=extension_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_extensions_delete(client):
    """Test case for virtual_machine_extensions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/extensions/{vm_extension_name}'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', vm_extension_name='vm_extension_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_extensions_get(client):
    """Test case for virtual_machine_extensions_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/extensions/{vm_extension_name}'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', vm_extension_name='vm_extension_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_extensions_list(client):
    """Test case for virtual_machine_extensions_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/extensions'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_extensions_update(client):
    """Test case for virtual_machine_extensions_update

    
    """
    extension_parameters = {"properties":{"settings":"{}","autoUpgradeMinorVersion":True,"publisher":"publisher","type":"type","forceUpdateTag":"forceUpdateTag","protectedSettings":"{}","typeHandlerVersion":"typeHandlerVersion"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}/extensions/{vm_extension_name}'.format(resource_group_name='resource_group_name_example', vm_name='vm_name_example', vm_extension_name='vm_extension_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=extension_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

