# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.instance_failover_group import InstanceFailoverGroup
from openapi_server.models.instance_failover_group_list_result import InstanceFailoverGroupListResult


pytestmark = pytest.mark.asyncio

async def test_instance_failover_groups_create_or_update(client):
    """Test case for instance_failover_groups_create_or_update

    
    """
    parameters = {"properties":{"replicationRole":"Primary","replicationState":"replicationState","partnerRegions":[{"replicationRole":"Primary","location":"location"},{"replicationRole":"Primary","location":"location"}],"managedInstancePairs":[{"partnerManagedInstanceId":"partnerManagedInstanceId","primaryManagedInstanceId":"primaryManagedInstanceId"},{"partnerManagedInstanceId":"partnerManagedInstanceId","primaryManagedInstanceId":"primaryManagedInstanceId"}],"readOnlyEndpoint":{"failoverPolicy":"Disabled"},"readWriteEndpoint":{"failoverWithDataLossGracePeriodMinutes":0,"failoverPolicy":"Manual"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/instanceFailoverGroups/{failover_group_name}'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_instance_failover_groups_delete(client):
    """Test case for instance_failover_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/instanceFailoverGroups/{failover_group_name}'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_instance_failover_groups_failover(client):
    """Test case for instance_failover_groups_failover

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/instanceFailoverGroups/{failover_group_name}/failover'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_instance_failover_groups_force_failover_allow_data_loss(client):
    """Test case for instance_failover_groups_force_failover_allow_data_loss

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/instanceFailoverGroups/{failover_group_name}/forceFailoverAllowDataLoss'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_instance_failover_groups_get(client):
    """Test case for instance_failover_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/instanceFailoverGroups/{failover_group_name}'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', failover_group_name='failover_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_instance_failover_groups_list_by_location(client):
    """Test case for instance_failover_groups_list_by_location

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/locations/{location_name}/instanceFailoverGroups'.format(resource_group_name='resource_group_name_example', location_name='location_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

