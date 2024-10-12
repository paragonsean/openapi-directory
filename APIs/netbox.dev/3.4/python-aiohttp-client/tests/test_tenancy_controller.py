# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contact import Contact
from openapi_server.models.contact_assignment import ContactAssignment
from openapi_server.models.contact_group import ContactGroup
from openapi_server.models.contact_role import ContactRole
from openapi_server.models.tenancy_contact_assignments_list200_response import TenancyContactAssignmentsList200Response
from openapi_server.models.tenancy_contact_groups_list200_response import TenancyContactGroupsList200Response
from openapi_server.models.tenancy_contact_roles_list200_response import TenancyContactRolesList200Response
from openapi_server.models.tenancy_contacts_list200_response import TenancyContactsList200Response
from openapi_server.models.tenancy_tenant_groups_list200_response import TenancyTenantGroupsList200Response
from openapi_server.models.tenancy_tenants_list200_response import TenancyTenantsList200Response
from openapi_server.models.tenant import Tenant
from openapi_server.models.tenant_group import TenantGroup
from openapi_server.models.writable_contact import WritableContact
from openapi_server.models.writable_contact_assignment import WritableContactAssignment
from openapi_server.models.writable_contact_group import WritableContactGroup
from openapi_server.models.writable_tenant import WritableTenant
from openapi_server.models.writable_tenant_group import WritableTenantGroup


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_assignments_bulk_delete(client):
    """Test case for tenancy_contact_assignments_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/contact-assignments/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_assignments_bulk_partial_update(client):
    """Test case for tenancy_contact_assignments_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":5,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","contact":0,"display":"display","id":6,"priority":"primary","object_id":2147483647,"url":"https://openapi-generator.tech","object":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/contact-assignments/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_assignments_bulk_update(client):
    """Test case for tenancy_contact_assignments_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":5,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","contact":0,"display":"display","id":6,"priority":"primary","object_id":2147483647,"url":"https://openapi-generator.tech","object":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/contact-assignments/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_assignments_create(client):
    """Test case for tenancy_contact_assignments_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":5,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","contact":0,"display":"display","id":6,"priority":"primary","object_id":2147483647,"url":"https://openapi-generator.tech","object":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/tenancy/contact-assignments/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_assignments_delete(client):
    """Test case for tenancy_contact_assignments_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/contact-assignments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_assignments_list(client):
    """Test case for tenancy_contact_assignments_list

    
    """
    params = [('id', 'id_example'),
                    ('content_type_id', 'content_type_id_example'),
                    ('object_id', 'object_id_example'),
                    ('priority', 'priority_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('content_type', 'content_type_example'),
                    ('contact_id', 'contact_id_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('content_type_id__n', 'content_type_id__n_example'),
                    ('object_id__n', 'object_id__n_example'),
                    ('object_id__lte', 'object_id__lte_example'),
                    ('object_id__lt', 'object_id__lt_example'),
                    ('object_id__gte', 'object_id__gte_example'),
                    ('object_id__gt', 'object_id__gt_example'),
                    ('priority__n', 'priority__n_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('content_type__n', 'content_type__n_example'),
                    ('contact_id__n', 'contact_id__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/contact-assignments/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_assignments_partial_update(client):
    """Test case for tenancy_contact_assignments_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":5,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","contact":0,"display":"display","id":6,"priority":"primary","object_id":2147483647,"url":"https://openapi-generator.tech","object":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/contact-assignments/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_assignments_read(client):
    """Test case for tenancy_contact_assignments_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/contact-assignments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_assignments_update(client):
    """Test case for tenancy_contact_assignments_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","role":5,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","contact":0,"display":"display","id":6,"priority":"primary","object_id":2147483647,"url":"https://openapi-generator.tech","object":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/contact-assignments/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_groups_bulk_delete(client):
    """Test case for tenancy_contact_groups_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/contact-groups/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_groups_bulk_partial_update(client):
    """Test case for tenancy_contact_groups_bulk_partial_update

    
    """
    body = {"parent":5,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","contact_count":6,"display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/contact-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_groups_bulk_update(client):
    """Test case for tenancy_contact_groups_bulk_update

    
    """
    body = {"parent":5,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","contact_count":6,"display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/contact-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_groups_create(client):
    """Test case for tenancy_contact_groups_create

    
    """
    body = {"parent":5,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","contact_count":6,"display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/tenancy/contact-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_groups_delete(client):
    """Test case for tenancy_contact_groups_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/contact-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_groups_list(client):
    """Test case for tenancy_contact_groups_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('parent_id', 'parent_id_example'),
                    ('parent', 'parent_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('parent__n', 'parent__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/contact-groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_groups_partial_update(client):
    """Test case for tenancy_contact_groups_partial_update

    
    """
    body = {"parent":5,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","contact_count":6,"display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/contact-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_groups_read(client):
    """Test case for tenancy_contact_groups_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/contact-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_groups_update(client):
    """Test case for tenancy_contact_groups_update

    
    """
    body = {"parent":5,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","contact_count":6,"display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"name":"name","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/contact-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_roles_bulk_delete(client):
    """Test case for tenancy_contact_roles_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/contact-roles/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_roles_bulk_partial_update(client):
    """Test case for tenancy_contact_roles_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/contact-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_roles_bulk_update(client):
    """Test case for tenancy_contact_roles_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/contact-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_roles_create(client):
    """Test case for tenancy_contact_roles_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/tenancy/contact-roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_roles_delete(client):
    """Test case for tenancy_contact_roles_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/contact-roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_roles_list(client):
    """Test case for tenancy_contact_roles_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/contact-roles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_roles_partial_update(client):
    """Test case for tenancy_contact_roles_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/contact-roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_roles_read(client):
    """Test case for tenancy_contact_roles_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/contact-roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contact_roles_update(client):
    """Test case for tenancy_contact_roles_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/contact-roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contacts_bulk_delete(client):
    """Test case for tenancy_contacts_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/contacts/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contacts_bulk_partial_update(client):
    """Test case for tenancy_contacts_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","link":"https://openapi-generator.tech","description":"description","title":"title","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"phone":"phone","name":"name","id":6,"email":"email","group":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/contacts/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contacts_bulk_update(client):
    """Test case for tenancy_contacts_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","link":"https://openapi-generator.tech","description":"description","title":"title","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"phone":"phone","name":"name","id":6,"email":"email","group":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/contacts/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contacts_create(client):
    """Test case for tenancy_contacts_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","link":"https://openapi-generator.tech","description":"description","title":"title","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"phone":"phone","name":"name","id":6,"email":"email","group":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/tenancy/contacts/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contacts_delete(client):
    """Test case for tenancy_contacts_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/contacts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contacts_list(client):
    """Test case for tenancy_contacts_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('title', 'title_example'),
                    ('phone', 'phone_example'),
                    ('email', 'email_example'),
                    ('address', 'address_example'),
                    ('link', 'link_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('title__n', 'title__n_example'),
                    ('title__ic', 'title__ic_example'),
                    ('title__nic', 'title__nic_example'),
                    ('title__iew', 'title__iew_example'),
                    ('title__niew', 'title__niew_example'),
                    ('title__isw', 'title__isw_example'),
                    ('title__nisw', 'title__nisw_example'),
                    ('title__ie', 'title__ie_example'),
                    ('title__nie', 'title__nie_example'),
                    ('title__empty', 'title__empty_example'),
                    ('phone__n', 'phone__n_example'),
                    ('phone__ic', 'phone__ic_example'),
                    ('phone__nic', 'phone__nic_example'),
                    ('phone__iew', 'phone__iew_example'),
                    ('phone__niew', 'phone__niew_example'),
                    ('phone__isw', 'phone__isw_example'),
                    ('phone__nisw', 'phone__nisw_example'),
                    ('phone__ie', 'phone__ie_example'),
                    ('phone__nie', 'phone__nie_example'),
                    ('phone__empty', 'phone__empty_example'),
                    ('email__n', 'email__n_example'),
                    ('email__ic', 'email__ic_example'),
                    ('email__nic', 'email__nic_example'),
                    ('email__iew', 'email__iew_example'),
                    ('email__niew', 'email__niew_example'),
                    ('email__isw', 'email__isw_example'),
                    ('email__nisw', 'email__nisw_example'),
                    ('email__ie', 'email__ie_example'),
                    ('email__nie', 'email__nie_example'),
                    ('email__empty', 'email__empty_example'),
                    ('address__n', 'address__n_example'),
                    ('address__ic', 'address__ic_example'),
                    ('address__nic', 'address__nic_example'),
                    ('address__iew', 'address__iew_example'),
                    ('address__niew', 'address__niew_example'),
                    ('address__isw', 'address__isw_example'),
                    ('address__nisw', 'address__nisw_example'),
                    ('address__ie', 'address__ie_example'),
                    ('address__nie', 'address__nie_example'),
                    ('address__empty', 'address__empty_example'),
                    ('link__n', 'link__n_example'),
                    ('link__ic', 'link__ic_example'),
                    ('link__nic', 'link__nic_example'),
                    ('link__iew', 'link__iew_example'),
                    ('link__niew', 'link__niew_example'),
                    ('link__isw', 'link__isw_example'),
                    ('link__nisw', 'link__nisw_example'),
                    ('link__ie', 'link__ie_example'),
                    ('link__nie', 'link__nie_example'),
                    ('link__empty', 'link__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/contacts/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contacts_partial_update(client):
    """Test case for tenancy_contacts_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","link":"https://openapi-generator.tech","description":"description","title":"title","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"phone":"phone","name":"name","id":6,"email":"email","group":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/contacts/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contacts_read(client):
    """Test case for tenancy_contacts_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/tenancy/contacts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_contacts_update(client):
    """Test case for tenancy_contacts_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","address":"address","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","link":"https://openapi-generator.tech","description":"description","title":"title","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"phone":"phone","name":"name","id":6,"email":"email","group":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/contacts/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenant_groups_bulk_delete(client):
    """Test case for tenancy_tenant_groups_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/tenant-groups/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenant_groups_bulk_partial_update(client):
    """Test case for tenancy_tenant_groups_bulk_partial_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"tenant_count":5,"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/tenant-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenant_groups_bulk_update(client):
    """Test case for tenancy_tenant_groups_bulk_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"tenant_count":5,"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/tenant-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenant_groups_create(client):
    """Test case for tenancy_tenant_groups_create

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"tenant_count":5,"name":"name","id":6,"slug":"slug"}
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
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('parent_id', 'parent_id_example'),
                    ('parent', 'parent_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('parent__n', 'parent__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"tenant_count":5,"name":"name","id":6,"slug":"slug"}
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
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"tenant_count":5,"name":"name","id":6,"slug":"slug"}
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

async def test_tenancy_tenants_bulk_delete(client):
    """Test case for tenancy_tenants_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/tenancy/tenants/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenants_bulk_partial_update(client):
    """Test case for tenancy_tenants_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","circuit_count":0,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":3,"cluster_count":6,"description":"description","vrf_count":7,"url":"https://openapi-generator.tech","ipaddress_count":2,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":4,"rack_count":9,"name":"name","virtualmachine_count":2,"prefix_count":7,"id":5,"device_count":1,"slug":"slug","group":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/tenancy/tenants/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenants_bulk_update(client):
    """Test case for tenancy_tenants_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","circuit_count":0,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":3,"cluster_count":6,"description":"description","vrf_count":7,"url":"https://openapi-generator.tech","ipaddress_count":2,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":4,"rack_count":9,"name":"name","virtualmachine_count":2,"prefix_count":7,"id":5,"device_count":1,"slug":"slug","group":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/tenancy/tenants/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tenancy_tenants_create(client):
    """Test case for tenancy_tenants_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","circuit_count":0,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":3,"cluster_count":6,"description":"description","vrf_count":7,"url":"https://openapi-generator.tech","ipaddress_count":2,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":4,"rack_count":9,"name":"name","virtualmachine_count":2,"prefix_count":7,"id":5,"device_count":1,"slug":"slug","group":5}
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
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","circuit_count":0,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":3,"cluster_count":6,"description":"description","vrf_count":7,"url":"https://openapi-generator.tech","ipaddress_count":2,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":4,"rack_count":9,"name":"name","virtualmachine_count":2,"prefix_count":7,"id":5,"device_count":1,"slug":"slug","group":5}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","circuit_count":0,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","site_count":3,"cluster_count":6,"description":"description","vrf_count":7,"url":"https://openapi-generator.tech","ipaddress_count":2,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"vlan_count":4,"rack_count":9,"name":"name","virtualmachine_count":2,"prefix_count":7,"id":5,"device_count":1,"slug":"slug","group":5}
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

