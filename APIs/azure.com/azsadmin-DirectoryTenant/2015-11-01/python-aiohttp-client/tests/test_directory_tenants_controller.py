# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.directory_tenant import DirectoryTenant
from openapi_server.models.directory_tenant_list import DirectoryTenantList


pytestmark = pytest.mark.asyncio

async def test_directory_tenants_create_or_update(client):
    """Test case for directory_tenants_create_or_update

    
    """
    new_tenant = {"properties":{"tenantId":"tenantId"}}
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/directoryTenants/{tenant}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', tenant='tenant_example'),
        headers=headers,
        json=new_tenant,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_directory_tenants_delete(client):
    """Test case for directory_tenants_delete

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/directoryTenants/{tenant}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', tenant='tenant_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_directory_tenants_get(client):
    """Test case for directory_tenants_get

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/directoryTenants/{tenant}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', tenant='tenant_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_directory_tenants_list(client):
    """Test case for directory_tenants_list

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Subscriptions.Admin/directoryTenants'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

