# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.managed_instance import ManagedInstance
from openapi_server.models.managed_instance_list_result import ManagedInstanceListResult
from openapi_server.models.managed_instance_update import ManagedInstanceUpdate


pytestmark = pytest.mark.asyncio

async def test_managed_instances_create_or_update(client):
    """Test case for managed_instances_create_or_update

    
    """
    parameters = {"identity":"{}","sku":"{}","properties":{"instancePoolId":"instancePoolId","subnetId":"subnetId","administratorLogin":"administratorLogin","sourceManagedInstanceId":"sourceManagedInstanceId","fullyQualifiedDomainName":"fullyQualifiedDomainName","publicDataEndpointEnabled":True,"restorePointInTime":"2000-01-23T04:56:07.000+00:00","licenseType":"LicenseIncluded","proxyOverride":"Proxy","administratorLoginPassword":"administratorLoginPassword","dnsZone":"dnsZone","timezoneId":"timezoneId","collation":"collation","state":"state","dnsZonePartner":"dnsZonePartner","storageSizeInGB":0,"managedInstanceCreateMode":"Default","vCores":6}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instances_delete(client):
    """Test case for managed_instances_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instances_get(client):
    """Test case for managed_instances_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instances_list(client):
    """Test case for managed_instances_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/managedInstances'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instances_list_by_instance_pool(client):
    """Test case for managed_instances_list_by_instance_pool

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/instancePools/{instance_pool_name}/managedInstances'.format(resource_group_name='resource_group_name_example', instance_pool_name='instance_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instances_list_by_resource_group(client):
    """Test case for managed_instances_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_instances_update(client):
    """Test case for managed_instances_update

    
    """
    parameters = {"sku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":0},"properties":{"instancePoolId":"instancePoolId","subnetId":"subnetId","administratorLogin":"administratorLogin","sourceManagedInstanceId":"sourceManagedInstanceId","fullyQualifiedDomainName":"fullyQualifiedDomainName","publicDataEndpointEnabled":True,"restorePointInTime":"2000-01-23T04:56:07.000+00:00","licenseType":"LicenseIncluded","proxyOverride":"Proxy","administratorLoginPassword":"administratorLoginPassword","dnsZone":"dnsZone","timezoneId":"timezoneId","collation":"collation","state":"state","dnsZonePartner":"dnsZonePartner","storageSizeInGB":0,"managedInstanceCreateMode":"Default","vCores":6},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/managedInstances/{managed_instance_name}'.format(resource_group_name='resource_group_name_example', managed_instance_name='managed_instance_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

