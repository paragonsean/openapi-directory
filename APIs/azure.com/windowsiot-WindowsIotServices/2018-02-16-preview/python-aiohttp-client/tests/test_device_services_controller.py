# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_service import DeviceService
from openapi_server.models.device_service_description_list_result import DeviceServiceDescriptionListResult
from openapi_server.models.error_details import ErrorDetails


pytestmark = pytest.mark.asyncio

async def test_services_create_or_update(client):
    """Test case for services_create_or_update

    Create or update the metadata of a Windows IoT Device Service.
    """
    device_service = {"etag":"etag","properties":{"adminDomainName":"adminDomainName","notes":"notes","quantity":0,"billingDomainName":"billingDomainName","startDate":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.WindowsIoT/deviceServices/{device_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', device_name='device_name_example'),
        headers=headers,
        json=device_service,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_delete(client):
    """Test case for services_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.WindowsIoT/deviceServices/{device_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', device_name='device_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_get(client):
    """Test case for services_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.WindowsIoT/deviceServices/{device_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', device_name='device_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list(client):
    """Test case for services_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.WindowsIoT/deviceServices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_list_by_resource_group(client):
    """Test case for services_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.WindowsIoT/deviceServices'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_update(client):
    """Test case for services_update

    Updates the metadata of a Windows IoT Device Service.
    """
    device_service = {"etag":"etag","properties":{"adminDomainName":"adminDomainName","notes":"notes","quantity":0,"billingDomainName":"billingDomainName","startDate":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.WindowsIoT/deviceServices/{device_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', device_name='device_name_example'),
        headers=headers,
        json=device_service,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

