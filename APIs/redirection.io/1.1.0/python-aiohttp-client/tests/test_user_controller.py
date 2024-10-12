# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_creation_write import UserCreationWrite
from openapi_server.models.user_edit_info import UserEditInfo
from openapi_server.models.user_list import UserList
from openapi_server.models.user_password import UserPassword
from openapi_server.models.user_read import UserRead


pytestmark = pytest.mark.asyncio

async def test_confirm_new_email_user_item(client):
    """Test case for confirm_new_email_user_item

    Retrieves a User resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}/confirm-new-email/{new_email_token}'.format(id='id_example', new_email_token='new_email_token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_item(client):
    """Test case for delete_user_item

    Removes the User resource.
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_edit_email_user_item(client):
    """Test case for edit_email_user_item

    Replaces the User resource.
    """
    user = openapi_server.UserEditInfo()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{id}/edit-email'.format(id='id_example'),
        headers=headers,
        json=user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_edit_info_user_item(client):
    """Test case for edit_info_user_item

    Replaces the User resource.
    """
    user = openapi_server.UserEditInfo()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{id}/edit-info'.format(id='id_example'),
        headers=headers,
        json=user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_edit_password_user_item(client):
    """Test case for edit_password_user_item

    Replaces the User resource.
    """
    user = openapi_server.UserEditInfo()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{id}/edit-password'.format(id='id_example'),
        headers=headers,
        json=user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forgot_password_user_item(client):
    """Test case for forgot_password_user_item

    Replaces the User resource.
    """
    user = openapi_server.UserPassword()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/forgot-password/{reset_token}'.format(reset_token='reset_token_example'),
        headers=headers,
        json=user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_collection(client):
    """Test case for get_user_collection

    Retrieves the collection of User resources.
    """
    params = [('organizationId', 'organization_id_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_item(client):
    """Test case for get_user_item

    Retrieves a User resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_user_collection(client):
    """Test case for post_user_collection

    Creates a User resource.
    """
    user = openapi_server.UserCreationWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users',
        headers=headers,
        json=user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

