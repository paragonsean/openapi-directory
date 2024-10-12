# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.api_keys import ApiKeys
from openapi_server.models.get_or_create_user_role200_response import GetOrCreateUserRole200Response
from openapi_server.models.permissions import Permissions
from openapi_server.models.role import Role


pytestmark = pytest.mark.asyncio

async def test_create_api_key(client):
    """Test case for create_api_key

    Create a new API key.
    """
    params = [('description', 'description_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apikeys/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_permissions(client):
    """Test case for get_all_permissions

    Get all permissions for the specified server.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/permissions'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_keys(client):
    """Test case for get_api_keys

    Get all API keys.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apikeys/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_or_create_user_role(client):
    """Test case for get_or_create_user_role

    Get or create a role for a specific user.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/users/{userid}/role'.format(serverid='serverid_example', userid='userid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_permissions(client):
    """Test case for get_permissions

    Get all permissions for the specified server and role.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/permissions/{roleid}'.format(serverid='serverid_example', roleid='roleid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_role(client):
    """Test case for get_user_role

    Get role for a specific user.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/users/{userid}/role'.format(serverid='serverid_example', userid='userid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_grant_permissions(client):
    """Test case for grant_permissions

    Set new permissions for the specified role on a server
    """
    permissions = ['permissions_example']
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/permissions/{roleid}'.format(serverid='serverid_example', roleid='roleid_example'),
        headers=headers,
        json=permissions,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_permissions(client):
    """Test case for revoke_permissions

    Revoke all permissions for the specified server and role.
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}/permissions/{roleid}'.format(serverid='serverid_example', roleid='roleid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

