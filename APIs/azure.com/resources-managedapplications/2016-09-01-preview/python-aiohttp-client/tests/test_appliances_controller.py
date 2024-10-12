# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.appliance import Appliance
from openapi_server.models.appliance_list_result import ApplianceListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_appliances_create_or_update(client):
    """Test case for appliances_create_or_update

    
    """
    parameters = {"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"outputs":"{}","uiDefinitionUri":"uiDefinitionUri","managedResourceGroupId":"managedResourceGroupId","provisioningState":"Accepted","parameters":"{}","applianceDefinitionId":"applianceDefinitionId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/appliances/{appliance_name}'.format(resource_group_name='resource_group_name_example', appliance_name='appliance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliances_create_or_update_by_id(client):
    """Test case for appliances_create_or_update_by_id

    
    """
    parameters = {"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"outputs":"{}","uiDefinitionUri":"uiDefinitionUri","managedResourceGroupId":"managedResourceGroupId","provisioningState":"Accepted","parameters":"{}","applianceDefinitionId":"applianceDefinitionId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{appliance_id}'.format(appliance_id='appliance_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliances_delete(client):
    """Test case for appliances_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/appliances/{appliance_name}'.format(resource_group_name='resource_group_name_example', appliance_name='appliance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliances_delete_by_id(client):
    """Test case for appliances_delete_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{appliance_id}'.format(appliance_id='appliance_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliances_get(client):
    """Test case for appliances_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/appliances/{appliance_name}'.format(resource_group_name='resource_group_name_example', appliance_name='appliance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliances_get_by_id(client):
    """Test case for appliances_get_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{appliance_id}'.format(appliance_id='appliance_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliances_list_by_resource_group(client):
    """Test case for appliances_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/appliances'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliances_list_by_subscription(client):
    """Test case for appliances_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Solutions/appliances'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliances_update(client):
    """Test case for appliances_update

    
    """
    parameters = {"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"outputs":"{}","uiDefinitionUri":"uiDefinitionUri","managedResourceGroupId":"managedResourceGroupId","provisioningState":"Accepted","parameters":"{}","applianceDefinitionId":"applianceDefinitionId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/appliances/{appliance_name}'.format(resource_group_name='resource_group_name_example', appliance_name='appliance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appliances_update_by_id(client):
    """Test case for appliances_update_by_id

    
    """
    parameters = {"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"outputs":"{}","uiDefinitionUri":"uiDefinitionUri","managedResourceGroupId":"managedResourceGroupId","provisioningState":"Accepted","parameters":"{}","applianceDefinitionId":"applianceDefinitionId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{appliance_id}'.format(appliance_id='appliance_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

