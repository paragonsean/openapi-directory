# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_change_password import AuthChangePassword
from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.place_created import PlaceCreated
from openapi_server.models.place_item import PlaceItem
from openapi_server.models.place_new import PlaceNew
from openapi_server.models.user import User
from openapi_server.models.user_created import UserCreated
from openapi_server.models.user_item import UserItem
from openapi_server.models.user_new import UserNew
from openapi_server.models.user_patch import UserPatch
from openapi_server.models.user_token_item import UserTokenItem


pytestmark = pytest.mark.asyncio

async def test_account_change_password(client):
    """Test case for account_change_password

    Change the password
    """
    change_password_info = {"oldPassword":"oldPassword","newPassword":"newPassword"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/account/change-password',
        headers=headers,
        json=change_password_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_delete_user(client):
    """Test case for account_delete_user

    Delete a User
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/account/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_user(client):
    """Test case for account_get_user

    Information about a User
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_new_place(client):
    """Test case for account_new_place

    Create a Place
    """
    place = {"country":"FR","zipCode":"zipCode","metadata":{},"name":"⌂ Home","timeZone":"Europe/Paris"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/account/places',
        headers=headers,
        json=place,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_new_user(client):
    """Test case for account_new_user

    New User
    """
    user_info = {"metadata":{},"phoneNumber":"+33177494646","name":"name","locale":"fr-FR","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/account/users',
        headers=headers,
        json=user_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_patch_user(client):
    """Test case for account_patch_user

    Modify a User
    """
    user_patch = {"phoneNumber":"+33177494646","name":"name","locale":"fr-FR","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/account/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        json=user_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_places(client):
    """Test case for account_places

    List Places of the Account
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/places',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_revoke_token(client):
    """Test case for account_revoke_token

    Revoke a Token
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/account/tokens/{token_id}'.format(token_id='token_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_tokens(client):
    """Test case for account_tokens

    List active Tokens of the Account
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/tokens',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_users(client):
    """Test case for account_users

    List Users of the Account
    """
    params = [('embed-metadata', ['embed_metadata_example'])]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_get_metadata(client):
    """Test case for user_get_metadata

    List metadata
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/account/users/{user_id}/metadata'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_patch_metadata(client):
    """Test case for user_patch_metadata

    Modify metadata
    """
    metadata_patch = {"add":{},"remove":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/account/users/{user_id}/metadata'.format(user_id='user_id_example'),
        headers=headers,
        json=metadata_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

