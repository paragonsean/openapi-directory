# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_list_result import ApplicationListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_applications_create_or_update(client):
    """Test case for applications_create_or_update

    
    """
    parameters = {"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"outputs":"{}","managedResourceGroupId":"managedResourceGroupId","provisioningState":"Accepted","applicationDefinitionId":"applicationDefinitionId","parameters":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications/{application_name}'.format(resource_group_name='resource_group_name_example', application_name='application_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_create_or_update_by_id(client):
    """Test case for applications_create_or_update_by_id

    
    """
    parameters = {"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"outputs":"{}","managedResourceGroupId":"managedResourceGroupId","provisioningState":"Accepted","applicationDefinitionId":"applicationDefinitionId","parameters":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{application_id}'.format(application_id='application_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_delete(client):
    """Test case for applications_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications/{application_name}'.format(resource_group_name='resource_group_name_example', application_name='application_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_delete_by_id(client):
    """Test case for applications_delete_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{application_id}'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_get(client):
    """Test case for applications_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications/{application_name}'.format(resource_group_name='resource_group_name_example', application_name='application_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_get_by_id(client):
    """Test case for applications_get_by_id

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{application_id}'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_list_by_resource_group(client):
    """Test case for applications_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_list_by_subscription(client):
    """Test case for applications_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Solutions/applications'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_update(client):
    """Test case for applications_update

    
    """
    parameters = {"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"outputs":"{}","managedResourceGroupId":"managedResourceGroupId","provisioningState":"Accepted","applicationDefinitionId":"applicationDefinitionId","parameters":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Solutions/applications/{application_name}'.format(resource_group_name='resource_group_name_example', application_name='application_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applications_update_by_id(client):
    """Test case for applications_update_by_id

    
    """
    parameters = {"kind":"kind","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher","version":"version"},"properties":{"outputs":"{}","managedResourceGroupId":"managedResourceGroupId","provisioningState":"Accepted","applicationDefinitionId":"applicationDefinitionId","parameters":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/{application_id}'.format(application_id='application_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

