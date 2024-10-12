# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email import Email
from openapi_server.models.event import Event
from openapi_server.models.post_v3_user_keys_request import PostV3UserKeysRequest
from openapi_server.models.post_v3_users_id_emails_request import PostV3UsersIdEmailsRequest
from openapi_server.models.post_v3_users_request import PostV3UsersRequest
from openapi_server.models.put_v3_users_id_request import PutV3UsersIdRequest
from openapi_server.models.ssh_key import SSHKey
from openapi_server.models.user_basic import UserBasic
from openapi_server.models.user_public import UserPublic


pytestmark = pytest.mark.asyncio

async def test_delete_v3_users_id(client):
    """Test case for delete_v3_users_id

    Delete a user. Available only for admins.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_users_id_emails_email_id(client):
    """Test case for delete_v3_users_id_emails_email_id

    Delete an email address of a specified user. Available only for admins.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/users/{id}/emails/{email_id}'.format(id=56, email_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_users_id_keys_key_id(client):
    """Test case for delete_v3_users_id_keys_key_id

    Delete an existing SSH key from a specified user. Available only for admins.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/users/{id}/keys/{key_id}'.format(id=56, key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_users(client):
    """Test case for get_v3_users

    Get the list of users
    """
    params = [('username', 'username_example'),
                    ('search', 'search_example'),
                    ('active', True),
                    ('external', True),
                    ('blocked', True),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_users_id(client):
    """Test case for get_v3_users_id

    Get a single user
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_users_id_emails(client):
    """Test case for get_v3_users_id_emails

    Get the emails addresses of a specified user. Available only for admins.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{id}/emails'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_users_id_events(client):
    """Test case for get_v3_users_id_events

    Get the contribution events of a specified user
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{id}/events'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_users_id_keys(client):
    """Test case for get_v3_users_id_keys

    Get the SSH keys of a specified user. Available only for admins.
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{id}/keys'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_users(client):
    """Test case for post_v3_users

    Create a user. Available only for admins.
    """
    body = openapi_server.PostV3UsersRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_users_id_emails(client):
    """Test case for post_v3_users_id_emails

    Add an email address to a specified user. Available only for admins.
    """
    body = openapi_server.PostV3UsersIdEmailsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/users/{id}/emails'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_users_id_keys(client):
    """Test case for post_v3_users_id_keys

    Add an SSH key to a specified user. Available only for admins.
    """
    body = openapi_server.PostV3UserKeysRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/users/{id}/keys'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_users_id(client):
    """Test case for put_v3_users_id

    Update a user. Available only for admins.
    """
    body = openapi_server.PutV3UsersIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/users/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_users_id_block(client):
    """Test case for put_v3_users_id_block

    Block a user. Available only for admins.
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/users/{id}/block'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_users_id_unblock(client):
    """Test case for put_v3_users_id_unblock

    Unblock a user. Available only for admins.
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/users/{id}/unblock'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

