# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.infra_role_instance import InfraRoleInstance
from openapi_server.models.infra_role_instance_list import InfraRoleInstanceList


pytestmark = pytest.mark.asyncio

async def test_infra_role_instances_get(client):
    """Test case for infra_role_instances_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances/{infra_role_instance}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', infra_role_instance='infra_role_instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_infra_role_instances_list(client):
    """Test case for infra_role_instances_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_infra_role_instances_power_off(client):
    """Test case for infra_role_instances_power_off

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances/{infra_role_instance}/PowerOff'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', infra_role_instance='infra_role_instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_infra_role_instances_power_on(client):
    """Test case for infra_role_instances_power_on

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances/{infra_role_instance}/PowerOn'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', infra_role_instance='infra_role_instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_infra_role_instances_reboot(client):
    """Test case for infra_role_instances_reboot

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances/{infra_role_instance}/Reboot'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', infra_role_instance='infra_role_instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_infra_role_instances_shutdown(client):
    """Test case for infra_role_instances_shutdown

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/infraRoleInstances/{infra_role_instance}/Shutdown'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', infra_role_instance='infra_role_instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

