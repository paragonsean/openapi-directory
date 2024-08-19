# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.rolling_upgrade_status_info import RollingUpgradeStatusInfo


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_rolling_upgrades_cancel(client):
    """Test case for virtual_machine_scale_set_rolling_upgrades_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/rollingUpgrades/cancel'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_rolling_upgrades_get_latest(client):
    """Test case for virtual_machine_scale_set_rolling_upgrades_get_latest

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/rollingUpgrades/latest'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_machine_scale_set_rolling_upgrades_start_os_upgrade(client):
    """Test case for virtual_machine_scale_set_rolling_upgrades_start_os_upgrade

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachineScaleSets/{vm_scale_set_name}/osRollingUpgrade'.format(resource_group_name='resource_group_name_example', vm_scale_set_name='vm_scale_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

