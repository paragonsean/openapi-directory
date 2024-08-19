# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email import Email
from openapi_server.models.email_data import EmailData
from openapi_server.models.email_error import EmailError
from openapi_server.models.not_found import NotFound
from openapi_server.models.user import User
from openapi_server.models.user_data import UserData
from openapi_server.models.user_error import UserError


pytestmark = pytest.mark.asyncio

async def test_me(client):
    """Test case for me

    A convenience endpoint that is equivalent to GET /v1/users/profiles/<my user id>/
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_avatar_delete(client):
    """Test case for user_avatar_delete

    Delete avatar
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/users/{user}/avatar'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_avatar_get(client):
    """Test case for user_avatar_get

    Retrieve user's avatar
    """
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user}/avatar'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_avatar_set(client):
    """Test case for user_avatar_set

    Add user avatar
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users/{user}/avatar'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_avatar_update(client):
    """Test case for user_avatar_update

    Update a project file
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/{user}/avatar'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_api_key_list(client):
    """Test case for users_api_key_list

    Retrieve account's API key
    """
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user}/api-key'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_create(client):
    """Test case for users_create

    Create new user
    """
    user_data = {"password":"password","profile":{"timezone":"timezone","bio":"bio","company":"company","location":"location","avatar":"avatar","url":"url"},"last_name":"last_name","first_name":"first_name","email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users/profiles/',
        headers=headers,
        json=user_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete(client):
    """Test case for users_delete

    Delete a user
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/users/profiles/{user}'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_emails_create(client):
    """Test case for users_emails_create

    Create an email address
    """
    email_data = {"unsubscribed":True,"address":"address","public":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users/{user}/emails'.format(user='user_example'),
        headers=headers,
        json=email_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_emails_delete(client):
    """Test case for users_emails_delete

    Delete an email address
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/users/{user}/emails/{email_id}'.format(email_id='email_id_example', user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_emails_list(client):
    """Test case for users_emails_list

    Retrieve account email addresses
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user}/emails'.format(user='user_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_emails_read(client):
    """Test case for users_emails_read

    Retrieve a user's email addresses
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user}/emails/{email_id}'.format(email_id='email_id_example', user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_emails_replace(client):
    """Test case for users_emails_replace

    Replace an email address
    """
    email_data = {"unsubscribed":True,"address":"address","public":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/users/{user}/emails/{email_id}'.format(email_id='email_id_example', user='user_example'),
        headers=headers,
        json=email_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_emails_update(client):
    """Test case for users_emails_update

    Update an email address
    """
    email_data = {"unsubscribed":True,"address":"address","public":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/{user}/emails/{email_id}'.format(email_id='email_id_example', user='user_example'),
        headers=headers,
        json=email_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list(client):
    """Test case for users_list

    Get user list
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('username', 'username_example'),
                    ('email', 'email_example'),
                    ('ordering', 'ordering_example')]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/profiles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_read(client):
    """Test case for users_read

    Retrieve a user
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/profiles/{user}'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ssh_key_list(client):
    """Test case for users_ssh_key_list

    Retrieve an SSH key
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user}/ssh-key'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_ssh_key_reset(client):
    """Test case for users_ssh_key_reset

    Recreate an SSH key
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users/{user}/ssh-key/reset'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update(client):
    """Test case for users_update

    Update a user
    """
    user_data = {"password":"password","profile":{"timezone":"timezone","bio":"bio","company":"company","location":"location","avatar":"avatar","url":"url"},"last_name":"last_name","first_name":"first_name","email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/profiles/{user}'.format(user='user_example'),
        headers=headers,
        json=user_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

