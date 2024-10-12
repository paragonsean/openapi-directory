# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_method_users_get_presence import APIMethodUsersGetPresence
from openapi_server.models.users_conversations_error_schema import UsersConversationsErrorSchema
from openapi_server.models.users_conversations_success_schema import UsersConversationsSuccessSchema
from openapi_server.models.users_counts_error_schema import UsersCountsErrorSchema
from openapi_server.models.users_delete_photo_error_schema import UsersDeletePhotoErrorSchema
from openapi_server.models.users_delete_photo_schema import UsersDeletePhotoSchema
from openapi_server.models.users_identity_error_schema import UsersIdentityErrorSchema
from openapi_server.models.users_identity_schema_inner import UsersIdentitySchemaInner
from openapi_server.models.users_info_error_schema import UsersInfoErrorSchema
from openapi_server.models.users_info_success_schema import UsersInfoSuccessSchema
from openapi_server.models.users_list_error_schema import UsersListErrorSchema
from openapi_server.models.users_list_schema import UsersListSchema
from openapi_server.models.users_lookup_by_email_error_schema import UsersLookupByEmailErrorSchema
from openapi_server.models.users_lookup_by_email_success_schema import UsersLookupByEmailSuccessSchema
from openapi_server.models.users_profile_get_error_schema import UsersProfileGetErrorSchema
from openapi_server.models.users_profile_get_schema import UsersProfileGetSchema
from openapi_server.models.users_profile_set_error_schema import UsersProfileSetErrorSchema
from openapi_server.models.users_profile_set_schema import UsersProfileSetSchema
from openapi_server.models.users_set_active_error_schema import UsersSetActiveErrorSchema
from openapi_server.models.users_set_active_schema import UsersSetActiveSchema
from openapi_server.models.users_set_photo_error_schema import UsersSetPhotoErrorSchema
from openapi_server.models.users_set_photo_schema import UsersSetPhotoSchema
from openapi_server.models.users_set_presence_error_schema import UsersSetPresenceErrorSchema
from openapi_server.models.users_set_presence_schema import UsersSetPresenceSchema


pytestmark = pytest.mark.asyncio

async def test_users_conversations(client):
    """Test case for users_conversations

    
    """
    params = [('token', 'token_example'),
                    ('user', 'user_example'),
                    ('types', 'types_example'),
                    ('exclude_archived', True),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users.conversations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_users_delete_photo(client):
    """Test case for users_delete_photo

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/users.deletePhoto',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get_presence(client):
    """Test case for users_get_presence

    
    """
    params = [('token', 'token_example'),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users.getPresence',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_identity(client):
    """Test case for users_identity

    
    """
    params = [('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users.identity',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_info(client):
    """Test case for users_info

    
    """
    params = [('token', 'token_example'),
                    ('include_locale', True),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list(client):
    """Test case for users_list

    
    """
    params = [('token', 'token_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('include_locale', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_lookup_by_email(client):
    """Test case for users_lookup_by_email

    
    """
    params = [('token', 'token_example'),
                    ('email', 'email_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users.lookupByEmail',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_profile_get_0(client):
    """Test case for users_profile_get_0

    
    """
    params = [('token', 'token_example'),
                    ('include_labels', True),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/users.profile.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_users_profile_set_0(client):
    """Test case for users_profile_set_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'name': 'name_example',
        'profile': 'profile_example',
        'user': 'user_example',
        'value': 'value_example'
        }
    response = await client.request(
        method='POST',
        path='/api/users.profile.set',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_set_active(client):
    """Test case for users_set_active

    
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users.setActive',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_users_set_photo(client):
    """Test case for users_set_photo

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'crop_w': 'crop_w_example',
        'crop_x': 'crop_x_example',
        'crop_y': 'crop_y_example',
        'image': 'image_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/users.setPhoto',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_users_set_presence(client):
    """Test case for users_set_presence

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'presence': 'presence_example'
        }
    response = await client.request(
        method='POST',
        path='/api/users.setPresence',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

