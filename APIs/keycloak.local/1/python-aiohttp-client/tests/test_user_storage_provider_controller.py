# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.synchronization_result import SynchronizationResult


pytestmark = pytest.mark.asyncio

async def test_id_name_get(client):
    """Test case for id_name_get

    Need this for admin console to display simple name of provider when displaying client detail   KEYCLOAK-4328
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{id}/name'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_user_storage_id_name_get(client):
    """Test case for realm_user_storage_id_name_get

    Need this for admin console to display simple name of provider when displaying user detail   KEYCLOAK-4328
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/user-storage/{id}/name'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_user_storage_id_remove_imported_users_post(client):
    """Test case for realm_user_storage_id_remove_imported_users_post

    Remove imported users
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/user-storage/{id}/remove-imported-users'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_user_storage_id_sync_post(client):
    """Test case for realm_user_storage_id_sync_post

    Trigger sync of users   Action can be \"triggerFullSync\" or \"triggerChangedUsersSync\"
    """
    params = [('action', 'action_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/user-storage/{id}/sync'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_user_storage_id_unlink_users_post(client):
    """Test case for realm_user_storage_id_unlink_users_post

    Unlink imported users from a storage provider
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/user-storage/{id}/unlink-users'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_user_storage_parent_id_mappers_id_sync_post(client):
    """Test case for realm_user_storage_parent_id_mappers_id_sync_post

    Trigger sync of mapper data related to ldap mapper (roles, groups, …​)   direction is \"fedToKeycloak\" or \"keycloakToFed\"
    """
    params = [('direction', 'direction_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/user-storage/{parent_id}/mappers/{id}/sync'.format(realm='realm_example', parent_id='parent_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

