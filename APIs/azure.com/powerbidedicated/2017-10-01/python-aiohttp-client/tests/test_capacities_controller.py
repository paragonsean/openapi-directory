# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_capacity_name_availability_parameters import CheckCapacityNameAvailabilityParameters
from openapi_server.models.check_capacity_name_availability_result import CheckCapacityNameAvailabilityResult
from openapi_server.models.dedicated_capacities import DedicatedCapacities
from openapi_server.models.dedicated_capacity import DedicatedCapacity
from openapi_server.models.dedicated_capacity_update_parameters import DedicatedCapacityUpdateParameters
from openapi_server.models.sku_enumeration_for_existing_resource_result import SkuEnumerationForExistingResourceResult


pytestmark = pytest.mark.asyncio

async def test_capacities_check_name_availability(client):
    """Test case for capacities_check_name_availability

    
    """
    capacity_parameters = {"name":"name","type":"Microsoft.PowerBIDedicated/capacities"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PowerBIDedicated/locations/{location}/checkNameAvailability'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=capacity_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capacities_create(client):
    """Test case for capacities_create

    
    """
    capacity_parameters = {"properties":{"provisioningState":"Deleting","state":"Deleting"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBIDedicated/capacities/{dedicated_capacity_name}'.format(resource_group_name='resource_group_name_example', dedicated_capacity_name='dedicated_capacity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=capacity_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capacities_delete(client):
    """Test case for capacities_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBIDedicated/capacities/{dedicated_capacity_name}'.format(resource_group_name='resource_group_name_example', dedicated_capacity_name='dedicated_capacity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capacities_get_details(client):
    """Test case for capacities_get_details

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBIDedicated/capacities/{dedicated_capacity_name}'.format(resource_group_name='resource_group_name_example', dedicated_capacity_name='dedicated_capacity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capacities_list(client):
    """Test case for capacities_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PowerBIDedicated/capacities'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capacities_list_by_resource_group(client):
    """Test case for capacities_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBIDedicated/capacities'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capacities_list_skus_for_capacity(client):
    """Test case for capacities_list_skus_for_capacity

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBIDedicated/capacities/{dedicated_capacity_name}/skus'.format(resource_group_name='resource_group_name_example', dedicated_capacity_name='dedicated_capacity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capacities_resume(client):
    """Test case for capacities_resume

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBIDedicated/capacities/{dedicated_capacity_name}/resume'.format(resource_group_name='resource_group_name_example', dedicated_capacity_name='dedicated_capacity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capacities_suspend(client):
    """Test case for capacities_suspend

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBIDedicated/capacities/{dedicated_capacity_name}/suspend'.format(resource_group_name='resource_group_name_example', dedicated_capacity_name='dedicated_capacity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_capacities_update(client):
    """Test case for capacities_update

    
    """
    capacity_update_parameters = {"sku":{"tier":"PBIE_Azure","name":"name"},"properties":{"administration":{"members":["members","members"]}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PowerBIDedicated/capacities/{dedicated_capacity_name}'.format(resource_group_name='resource_group_name_example', dedicated_capacity_name='dedicated_capacity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=capacity_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

