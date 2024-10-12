# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.role_info import RoleInfo
from openapi_server.models.role_info_create import RoleInfoCreate
from openapi_server.models.role_info_list_response import RoleInfoListResponse
from openapi_server.models.role_info_update import RoleInfoUpdate


pytestmark = pytest.mark.asyncio

async def test_create_role(client):
    """Test case for create_role

    Create a new role
    """
    body = {"organizationId":"organizationId","roleTemplate":"roleTemplate","name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/role',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_role(client):
    """Test case for delete_role

    Delete a role
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/role/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_role(client):
    """Test case for get_role

    Get role information for the specified role
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/role/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_roles(client):
    """Test case for get_roles

    Get all roles in an organization
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('sort_by', Name),
                    ('sort_order', asc),
                    ('organization_id', 'organization_id_example'),
                    ('name', 'name_example'),
                    ('role_template', ['role_template_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/role',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_role(client):
    """Test case for update_role

    Update role information
    """
    body = {"name":"name","description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/role/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

