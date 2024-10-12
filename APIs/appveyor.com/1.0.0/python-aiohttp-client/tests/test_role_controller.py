# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.role import Role
from openapi_server.models.role_addition import RoleAddition
from openapi_server.models.role_with_groups import RoleWithGroups


pytestmark = pytest.mark.asyncio

async def test_add_role(client):
    """Test case for add_role

    Add role
    """
    body = {"name":"My Role"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/roles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_role(client):
    """Test case for delete_role

    Delete role
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/roles/{role_id}'.format(role_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_role(client):
    """Test case for get_role

    Get role
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/roles/{role_id}'.format(role_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_roles(client):
    """Test case for get_roles

    Get roles
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/roles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_role(client):
    """Test case for update_role

    Update role
    """
    body = {"isSystem":True,"created":"2000-01-23T04:56:07.000+00:00","roleId":0,"name":"name","groups":[{"permissions":[{"allowed":True,"name":"ManageApplicationAuthorizations","description":"description"},{"allowed":True,"name":"ManageApplicationAuthorizations","description":"description"}],"name":"Account"},{"permissions":[{"allowed":True,"name":"ManageApplicationAuthorizations","description":"description"},{"allowed":True,"name":"ManageApplicationAuthorizations","description":"description"}],"name":"Account"}],"updated":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/roles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

