# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tenancy_tenant_groups_list200_response import TenancyTenantGroupsList200Response
from openapi_server.models.tenancy_tenants_list200_response import TenancyTenantsList200Response
from openapi_server.models.tenant import Tenant
from openapi_server.models.tenant_group import TenantGroup
from openapi_server.models.writable_tenant import WritableTenant


pytestmark = pytest.mark.asyncio

async def test_tenancy_choices_list(client):
    """Test case for tenancy_choices_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/_choices/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_choices_read(client):
    """Test case for tenancy_choices_read

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/_choices/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenant_groups_create(client):
    """Test case for tenancy_tenant_groups_create

    
    """
    body = {"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/tenancy/tenant-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenant_groups_delete(client):
    """Test case for tenancy_tenant_groups_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/tenant-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenant_groups_list(client):
    """Test case for tenancy_tenant_groups_list

    
    """
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/tenant-groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenant_groups_partial_update(client):
    """Test case for tenancy_tenant_groups_partial_update

    
    """
    body = {"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/tenant-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenant_groups_read(client):
    """Test case for tenancy_tenant_groups_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/tenant-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenant_groups_update(client):
    """Test case for tenancy_tenant_groups_update

    
    """
    body = {"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/tenant-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenants_create(client):
    """Test case for tenancy_tenants_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","name":"name","description":"description","id":6,"slug":"slug","group":0,"tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/tenancy/tenants/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenants_delete(client):
    """Test case for tenancy_tenants_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/tenants/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenants_list(client):
    """Test case for tenancy_tenants_list

    
    """
    params = [('name', 'name_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('tag', 'tag_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/tenants/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenants_partial_update(client):
    """Test case for tenancy_tenants_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","name":"name","description":"description","id":6,"slug":"slug","group":0,"tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/tenants/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenants_read(client):
    """Test case for tenancy_tenants_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/tenants/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenants_update(client):
    """Test case for tenancy_tenants_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","name":"name","description":"description","id":6,"slug":"slug","group":0,"tags":["tags","tags"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/tenants/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

