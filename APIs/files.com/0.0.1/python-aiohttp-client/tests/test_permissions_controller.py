# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.permission_entity import PermissionEntity


pytestmark = pytest.mark.asyncio

async def test_delete_permissions_id(client):
    """Test case for delete_permissions_id

    Delete Permission
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/permissions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permissions(client):
    """Test case for get_permissions

    List Permissions
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_prefix', None),
                    ('path', 'path_example'),
                    ('group_id', 'group_id_example'),
                    ('user_id', 'user_id_example'),
                    ('include_groups', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/permissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_permissions(client):
    """Test case for post_permissions

    Create Permission
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('group_id', 56)
    data.add_field('path', 'path_example')
    data.add_field('permission', 'permission_example')
    data.add_field('recursive', True)
    data.add_field('user_id', 56)
    data.add_field('username', 'username_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/permissions',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

