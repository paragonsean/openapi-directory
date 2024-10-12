# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.permission_grant import PermissionGrant
from openapi_server.models.permission_grants import PermissionGrants
from openapi_server.models.permission_scheme import PermissionScheme
from openapi_server.models.permission_schemes import PermissionSchemes


pytestmark = pytest.mark.asyncio

async def test_create_permission_grant(client):
    """Test case for create_permission_grant

    Create permission grant
    """
    body = {"self":"https://openapi-generator.tech","holder":"","permission":"permission","id":6}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/permissionscheme/{scheme_id}/permission'.format(scheme_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_permission_scheme(client):
    """Test case for create_permission_scheme

    Create permission scheme
    """
    body = {"expand":"expand","permissions":[{"self":"https://openapi-generator.tech","holder":"","permission":"permission","id":6},{"self":"https://openapi-generator.tech","holder":"","permission":"permission","id":6}],"scope":"","name":"name","description":"description","self":"https://openapi-generator.tech","id":0}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/permissionscheme',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_permission_scheme(client):
    """Test case for delete_permission_scheme

    Delete permission scheme
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/permissionscheme/{scheme_id}'.format(scheme_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_permission_scheme_entity(client):
    """Test case for delete_permission_scheme_entity

    Delete permission scheme grant
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/permissionscheme/{scheme_id}/permission/{permission_id}'.format(scheme_id=56, permission_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_permission_schemes(client):
    """Test case for get_all_permission_schemes

    Get all permission schemes
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/permissionscheme',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permission_scheme(client):
    """Test case for get_permission_scheme

    Get permission scheme
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/permissionscheme/{scheme_id}'.format(scheme_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permission_scheme_grant(client):
    """Test case for get_permission_scheme_grant

    Get permission scheme grant
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/permissionscheme/{scheme_id}/permission/{permission_id}'.format(scheme_id=56, permission_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permission_scheme_grants(client):
    """Test case for get_permission_scheme_grants

    Get permission scheme grants
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/permissionscheme/{scheme_id}/permission'.format(scheme_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_permission_scheme(client):
    """Test case for update_permission_scheme

    Update permission scheme
    """
    body = {"expand":"expand","permissions":[{"self":"https://openapi-generator.tech","holder":"","permission":"permission","id":6},{"self":"https://openapi-generator.tech","holder":"","permission":"permission","id":6}],"scope":"","name":"name","description":"description","self":"https://openapi-generator.tech","id":0}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/permissionscheme/{scheme_id}'.format(scheme_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

