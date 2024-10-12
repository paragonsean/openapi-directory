# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apps_response import AppsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_response import UserResponse
from openapi_server.models.user_update_request import UserUpdateRequest
from openapi_server.models.user_visible_apps_linkages_request import UserVisibleAppsLinkagesRequest
from openapi_server.models.user_visible_apps_linkages_response import UserVisibleAppsLinkagesResponse
from openapi_server.models.users_response import UsersResponse


pytestmark = pytest.mark.asyncio

async def test_users_delete_instance(client):
    """Test case for users_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_collection(client):
    """Test case for users_get_collection

    
    """
    params = [('filter[roles]', ['filter_roles_example']),
                    ('filter[username]', ['filter_username_example']),
                    ('filter[visibleApps]', ['filter_visible_apps_example']),
                    ('sort', ['sort_example']),
                    ('fields[users]', ['fields_users_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[visibleApps]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_instance(client):
    """Test case for users_get_instance

    
    """
    params = [('fields[users]', ['fields_users_example']),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[visibleApps]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update_instance(client):
    """Test case for users_update_instance

    
    """
    body = {"data":{"relationships":{"visibleApps":{"data":[{"id":"id","type":"apps"},{"id":"id","type":"apps"}]}},"attributes":{"roles":["ADMIN","ADMIN"],"allAppsVisible":True,"provisioningAllowed":True},"id":"id","type":"users"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_visible_apps_create_to_many_relationship(client):
    """Test case for users_visible_apps_create_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"apps"},{"id":"id","type":"apps"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users/{id}/relationships/visibleApps'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_visible_apps_delete_to_many_relationship(client):
    """Test case for users_visible_apps_delete_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"apps"},{"id":"id","type":"apps"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/users/{id}/relationships/visibleApps'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_visible_apps_get_to_many_related(client):
    """Test case for users_visible_apps_get_to_many_related

    
    """
    params = [('fields[apps]', ['fields_apps_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{id}/visibleApps'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_visible_apps_get_to_many_relationship(client):
    """Test case for users_visible_apps_get_to_many_relationship

    
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{id}/relationships/visibleApps'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_visible_apps_replace_to_many_relationship(client):
    """Test case for users_visible_apps_replace_to_many_relationship

    
    """
    body = {"data":[{"id":"id","type":"apps"},{"id":"id","type":"apps"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/{id}/relationships/visibleApps'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

