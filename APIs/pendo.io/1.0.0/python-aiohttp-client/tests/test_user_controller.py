# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.end_user_ping import EndUserPing
from openapi_server.models.user import User
from openapi_server.models.users_id_put_request import UsersIdPutRequest
from openapi_server.models.users_invite_end_user_post_request import UsersInviteEndUserPostRequest
from openapi_server.models.users_invite_vendor_user_post_request import UsersInviteVendorUserPostRequest
from openapi_server.models.vendor_users_post_request import VendorUsersPostRequest


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    fetch User records
    """
    params = [('role', 'role_example'),
                    ('account', 56),
                    ('start', 0),
                    ('limit', 300),
                    ('order_by', 'order_by_example'),
                    ('order_dir', 'order_dir_example')]
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_delete(client):
    """Test case for users_id_delete

    Delete a User
    """
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{id}'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_get(client):
    """Test case for users_id_get

    Get a User record
    """
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_users_id_put(client):
    """Test case for users_id_put

    Update a User
    """
    user = openapi_server.UsersIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{id}'.format(id=3.4),
        headers=headers,
        json=user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_tags_delete(client):
    """Test case for users_id_tags_delete

    Delete custom User tags
    """
    headers = { 
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{id}/tags'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_tags_get(client):
    """Test case for users_id_tags_get

    Get custom User tags
    """
    headers = { 
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/tags'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_users_id_tags_post(client):
    """Test case for users_id_tags_post

    Overwrite current custom User tags with the given tags
    """
    tags = None
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{id}/tags'.format(id=3.4),
        headers=headers,
        json=tags,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_users_invite_end_user_post(client):
    """Test case for users_invite_end_user_post

    Invite an EndUser (customer)
    """
    data = openapi_server.UsersInviteEndUserPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/invite_end_user',
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_invite_vendor_user_post(client):
    """Test case for users_invite_vendor_user_post

    Invite a VendorUser (Team member)
    """
    data = openapi_server.UsersInviteVendorUserPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/invite_vendor_user',
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_post(client):
    """Test case for users_post

    Ping to create or update an EndUser and Account in one call
    """
    data = {"return_url":"return_url","user":{"full_name":"full_name","roles":"endUser","created_at":"created_at","id":"id","allowed_products":["allowed_products","allowed_products"],"email":"email","tags":"{}"},"account":{"name":"name","created_at":"created_at","is_paying":True,"id":"id","monthly_value":0.8008282,"status":"status","tags":"{}"}}
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users',
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_search_get(client):
    """Test case for users_search_get

    Find a User with a query
    """
    params = [('external_id', 'external_id_example'),
                    ('email', 'email_example'),
                    ('role', 'role_example')]
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vendor_users_post(client):
    """Test case for vendor_users_post

    Create or update a team member by their external_id
    """
    data = openapi_server.VendorUsersPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/vendor_users',
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

