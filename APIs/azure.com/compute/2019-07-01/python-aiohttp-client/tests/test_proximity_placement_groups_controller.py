# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.proximity_placement_group import ProximityPlacementGroup
from openapi_server.models.proximity_placement_group_list_result import ProximityPlacementGroupListResult
from openapi_server.models.proximity_placement_group_update import ProximityPlacementGroupUpdate


pytestmark = pytest.mark.asyncio

async def test_proximity_placement_groups_create_or_update(client):
    """Test case for proximity_placement_groups_create_or_update

    
    """
    parameters = {"properties":{"colocationStatus":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},"proximityPlacementGroupType":"Standard","virtualMachineScaleSets":[{"colocationStatus":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},{"colocationStatus":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}}],"availabilitySets":[{"colocationStatus":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},{"colocationStatus":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}}],"virtualMachines":[{"colocationStatus":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}},{"colocationStatus":{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/proximityPlacementGroups/{proximity_placement_group_name}'.format(resource_group_name='resource_group_name_example', proximity_placement_group_name='proximity_placement_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proximity_placement_groups_delete(client):
    """Test case for proximity_placement_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/proximityPlacementGroups/{proximity_placement_group_name}'.format(resource_group_name='resource_group_name_example', proximity_placement_group_name='proximity_placement_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proximity_placement_groups_get(client):
    """Test case for proximity_placement_groups_get

    
    """
    params = [('includeColocationStatus', 'include_colocation_status_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/proximityPlacementGroups/{proximity_placement_group_name}'.format(resource_group_name='resource_group_name_example', proximity_placement_group_name='proximity_placement_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proximity_placement_groups_list_by_resource_group(client):
    """Test case for proximity_placement_groups_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/proximityPlacementGroups'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proximity_placement_groups_list_by_subscription(client):
    """Test case for proximity_placement_groups_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/proximityPlacementGroups'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_proximity_placement_groups_update(client):
    """Test case for proximity_placement_groups_update

    
    """
    parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/proximityPlacementGroups/{proximity_placement_group_name}'.format(resource_group_name='resource_group_name_example', proximity_placement_group_name='proximity_placement_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

