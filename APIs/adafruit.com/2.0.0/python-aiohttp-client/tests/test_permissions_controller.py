# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_permission_request import CreatePermissionRequest
from openapi_server.models.permission import Permission


pytestmark = pytest.mark.asyncio

async def test_all_permissions(client):
    """Test case for all_permissions

    All permissions for current user and type
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/{type}/{type_id}/acl'.format(username='username_example', type='type_example', type_id='type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_permission(client):
    """Test case for create_permission

    Create a new Permission
    """
    permission = openapi_server.CreatePermissionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/{type}/{type_id}/acl'.format(username='username_example', type='type_example', type_id='type_id_example'),
        headers=headers,
        json=permission,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destroy_permission(client):
    """Test case for destroy_permission

    Delete an existing Permission
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/{username}/{type}/{type_id}/acl/{id}'.format(username='username_example', type='type_example', type_id='type_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permission(client):
    """Test case for get_permission

    Returns Permission based on ID
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/{type}/{type_id}/acl/{id}'.format(username='username_example', type='type_example', type_id='type_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_replace_permission(client):
    """Test case for replace_permission

    Replace an existing Permission
    """
    permission = openapi_server.CreatePermissionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/{username}/{type}/{type_id}/acl/{id}'.format(username='username_example', type='type_example', type_id='type_id_example', id='id_example'),
        headers=headers,
        json=permission,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_permission(client):
    """Test case for update_permission

    Update properties of an existing Permission
    """
    permission = openapi_server.CreatePermissionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/{username}/{type}/{type_id}/acl/{id}'.format(username='username_example', type='type_example', type_id='type_id_example', id='id_example'),
        headers=headers,
        json=permission,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

