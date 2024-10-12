# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.controller_power_state_change_request import ControllerPowerStateChangeRequest
from openapi_server.models.hardware_component_group_list import HardwareComponentGroupList


pytestmark = pytest.mark.asyncio

async def test_hardware_component_groups_change_controller_power_state(client):
    """Test case for hardware_component_groups_change_controller_power_state

    
    """
    parameters = {"properties":{"controller1State":"NotPresent","action":"Start","controller0State":"NotPresent","activeController":"Unknown"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/hardwareComponentGroups/{hardware_component_group_name}/changeControllerPowerState'.format(device_name='device_name_example', hardware_component_group_name='hardware_component_group_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hardware_component_groups_list_by_device(client):
    """Test case for hardware_component_groups_list_by_device

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/hardwareComponentGroups'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

