# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email import Email
from openapi_server.models.post_v3_user_emails_request import PostV3UserEmailsRequest
from openapi_server.models.post_v3_user_keys_request import PostV3UserKeysRequest
from openapi_server.models.ssh_key import SSHKey
from openapi_server.models.user_public import UserPublic


pytestmark = pytest.mark.asyncio

async def test_delete_v3_user_emails_email_id(client):
    """Test case for delete_v3_user_emails_email_id

    Delete an email address from the currently authenticated user
    """
    headers = { 
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/user/emails/{email_id}'.format(email_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_v3_user_keys_key_id(client):
    """Test case for delete_v3_user_keys_key_id

    Delete an SSH key from the currently authenticated user
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/user/keys/{key_id}'.format(key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_user(client):
    """Test case for get_v3_user

    Get the currently authenticated user
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_user_emails(client):
    """Test case for get_v3_user_emails

    Get the currently authenticated user's email addresses
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/emails',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_user_emails_email_id(client):
    """Test case for get_v3_user_emails_email_id

    Get a single email address owned by the currently authenticated user
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/emails/{email_id}'.format(email_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_user_keys(client):
    """Test case for get_v3_user_keys

    Get the currently authenticated user's SSH keys
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/keys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_v3_user_keys_key_id(client):
    """Test case for get_v3_user_keys_key_id

    Get a single key owned by currently authenticated user
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/keys/{key_id}'.format(key_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_user_emails(client):
    """Test case for post_v3_user_emails

    Add new email address to the currently authenticated user
    """
    body = openapi_server.PostV3UserEmailsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/user/emails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_v3_user_keys(client):
    """Test case for post_v3_user_keys

    Add a new SSH key to the currently authenticated user
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
        path='/api/v3/user/keys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

