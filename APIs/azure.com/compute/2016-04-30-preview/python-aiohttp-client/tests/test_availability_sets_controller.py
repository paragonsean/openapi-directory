# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.availability_set import AvailabilitySet
from openapi_server.models.availability_set_list_result import AvailabilitySetListResult
from openapi_server.models.operation_status_response import OperationStatusResponse
from openapi_server.models.virtual_machine_size_list_result import VirtualMachineSizeListResult


pytestmark = pytest.mark.asyncio

async def test_availability_sets_create_or_update(client):
    """Test case for availability_sets_create_or_update

    
    """
    parameters = {"sku":{"tier":"tier","name":"name","capacity":1},"properties":{"platformFaultDomainCount":0,"managed":True,"platformUpdateDomainCount":6,"statuses":[{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"},{"code":"code","level":"Info","displayStatus":"displayStatus","time":"2000-01-23T04:56:07.000+00:00","message":"message"}],"virtualMachines":[{"id":"id"},{"id":"id"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/availabilitySets/{availability_set_name}'.format(resource_group_name='resource_group_name_example', availability_set_name='availability_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_availability_sets_delete(client):
    """Test case for availability_sets_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/availabilitySets/{availability_set_name}'.format(resource_group_name='resource_group_name_example', availability_set_name='availability_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_availability_sets_get(client):
    """Test case for availability_sets_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/availabilitySets/{availability_set_name}'.format(resource_group_name='resource_group_name_example', availability_set_name='availability_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_availability_sets_list(client):
    """Test case for availability_sets_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/availabilitySets'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_availability_sets_list_available_sizes(client):
    """Test case for availability_sets_list_available_sizes

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/availabilitySets/{availability_set_name}/vmSizes'.format(resource_group_name='resource_group_name_example', availability_set_name='availability_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_availability_sets_list_by_subscription(client):
    """Test case for availability_sets_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/availabilitySets'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

