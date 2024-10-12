# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.basic_error import BasicError
from openapi_server.models.email import Email
from openapi_server.models.gpg_key import GpgKey
from openapi_server.models.hovercard import Hovercard
from openapi_server.models.key import Key
from openapi_server.models.key_simple import KeySimple
from openapi_server.models.private_user import PrivateUser
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.users_add_email_for_authenticated_request import UsersAddEmailForAuthenticatedRequest
from openapi_server.models.users_create_gpg_key_for_authenticated_request import UsersCreateGpgKeyForAuthenticatedRequest
from openapi_server.models.users_create_public_ssh_key_for_authenticated_request import UsersCreatePublicSshKeyForAuthenticatedRequest
from openapi_server.models.users_delete_email_for_authenticated_request import UsersDeleteEmailForAuthenticatedRequest
from openapi_server.models.users_get_authenticated200_response import UsersGetAuthenticated200Response
from openapi_server.models.users_update_authenticated_request import UsersUpdateAuthenticatedRequest
from openapi_server.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_users_add_email_for_authenticated(client):
    """Test case for users_add_email_for_authenticated

    Add an email address for the authenticated user
    """
    body = openapi_server.UsersAddEmailForAuthenticatedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/user/emails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_check_following_for_user(client):
    """Test case for users_check_following_for_user

    Check if a user follows another user
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/following/{target_user}'.format(username='username_example', target_user='target_user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_check_person_is_followed_by_authenticated(client):
    """Test case for users_check_person_is_followed_by_authenticated

    Check if a person is followed by the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/following/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_create_gpg_key_for_authenticated(client):
    """Test case for users_create_gpg_key_for_authenticated

    Create a GPG key for the authenticated user
    """
    body = openapi_server.UsersCreateGpgKeyForAuthenticatedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/user/gpg_keys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_create_public_ssh_key_for_authenticated(client):
    """Test case for users_create_public_ssh_key_for_authenticated

    Create a public SSH key for the authenticated user
    """
    body = openapi_server.UsersCreatePublicSshKeyForAuthenticatedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/user/keys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete_email_for_authenticated(client):
    """Test case for users_delete_email_for_authenticated

    Delete an email address for the authenticated user
    """
    body = openapi_server.UsersDeleteEmailForAuthenticatedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/user/emails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete_gpg_key_for_authenticated(client):
    """Test case for users_delete_gpg_key_for_authenticated

    Delete a GPG key for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/user/gpg_keys/{gpg_key_id}'.format(gpg_key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete_public_ssh_key_for_authenticated(client):
    """Test case for users_delete_public_ssh_key_for_authenticated

    Delete a public SSH key for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/user/keys/{key_id}'.format(key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_follow(client):
    """Test case for users_follow

    Follow a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/user/following/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_authenticated(client):
    """Test case for users_get_authenticated

    Get the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_by_username(client):
    """Test case for users_get_by_username

    Get a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_context_for_user(client):
    """Test case for users_get_context_for_user

    Get contextual information for a user
    """
    params = [('subject_type', 'subject_type_example'),
                    ('subject_id', 'subject_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/hovercard'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_gpg_key_for_authenticated(client):
    """Test case for users_get_gpg_key_for_authenticated

    Get a GPG key for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/gpg_keys/{gpg_key_id}'.format(gpg_key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_public_ssh_key_for_authenticated(client):
    """Test case for users_get_public_ssh_key_for_authenticated

    Get a public SSH key for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/keys/{key_id}'.format(key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list(client):
    """Test case for users_list

    List users
    """
    params = [('since', 56),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_emails_for_authenticated(client):
    """Test case for users_list_emails_for_authenticated

    List email addresses for the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/emails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_followed_by_authenticated(client):
    """Test case for users_list_followed_by_authenticated

    List the people the authenticated user follows
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/following',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_followers_for_authenticated_user(client):
    """Test case for users_list_followers_for_authenticated_user

    List followers of the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/followers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_followers_for_user(client):
    """Test case for users_list_followers_for_user

    List followers of a user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/followers'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_following_for_user(client):
    """Test case for users_list_following_for_user

    List the people a user follows
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/following'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_gpg_keys_for_authenticated(client):
    """Test case for users_list_gpg_keys_for_authenticated

    List GPG keys for the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/gpg_keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_gpg_keys_for_user(client):
    """Test case for users_list_gpg_keys_for_user

    List GPG keys for a user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/gpg_keys'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_public_emails_for_authenticated(client):
    """Test case for users_list_public_emails_for_authenticated

    List public email addresses for the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/public_emails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_public_keys_for_user(client):
    """Test case for users_list_public_keys_for_user

    List public keys for a user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/keys'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_public_ssh_keys_for_authenticated(client):
    """Test case for users_list_public_ssh_keys_for_authenticated

    List public SSH keys for the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_unfollow(client):
    """Test case for users_unfollow

    Unfollow a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/user/following/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update_authenticated(client):
    """Test case for users_update_authenticated

    Update the authenticated user
    """
    body = openapi_server.UsersUpdateAuthenticatedRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

