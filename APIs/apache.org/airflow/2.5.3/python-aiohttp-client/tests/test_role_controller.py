# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.role import Role
from openapi_server.models.role_collection import RoleCollection


pytestmark = pytest.mark.asyncio

async def test_delete_role(client):
    """Test case for delete_role

    Delete a role
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/roles/{role_name}'.format(role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_role(client):
    """Test case for get_role

    Get a role
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/roles/{role_name}'.format(role_name='role_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_roles(client):
    """Test case for get_roles

    List roles
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/roles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_role(client):
    """Test case for patch_role

    Update a role
    """
    body = {"name":"name","actions":[{"resource":{"name":"name"},"action":{"name":"name"}},{"resource":{"name":"name"},"action":{"name":"name"}}]}
    params = [('update_mask', ['update_mask_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/roles/{role_name}'.format(role_name='role_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_role(client):
    """Test case for post_role

    Create a role
    """
    body = {"name":"name","actions":[{"resource":{"name":"name"},"action":{"name":"name"}},{"resource":{"name":"name"},"action":{"name":"name"}}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/roles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

