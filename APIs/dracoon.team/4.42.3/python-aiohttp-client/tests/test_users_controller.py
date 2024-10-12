# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attributes_response import AttributesResponse
from openapi_server.models.create_user_request import CreateUserRequest
from openapi_server.models.emergency_mfa_code_response import EmergencyMfaCodeResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.last_admin_user_room_list import LastAdminUserRoomList
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.role_list import RoleList
from openapi_server.models.room_tree_data_list import RoomTreeDataList
from openapi_server.models.update_user_request import UpdateUserRequest
from openapi_server.models.user_attributes import UserAttributes
from openapi_server.models.user_data import UserData
from openapi_server.models.user_group_list import UserGroupList
from openapi_server.models.user_list import UserList


pytestmark = pytest.mark.asyncio

async def test_create_user(client):
    """Test case for create_user

    Create new user
    """
    body = {"isNonmemberViewer":True,"lastName":"lastName","needsToChangePassword":True,"gender":"n","receiverLanguage":"receiverLanguage","authData":{"password":"password","method":"method","adConfigId":0,"mustChangePassword":True,"login":"login","oidConfigId":6},"notifyUser":True,"authMethods":[{"isEnabled":True,"options":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"authId":"authId"},{"isEnabled":True,"options":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"authId":"authId"}],"login":"login","title":"title","userName":"userName","firstName":"firstName","password":"password","phone":"phone","mfaConfig":{"mfaEnforced":True},"expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user(client):
    """Test case for remove_user

    Remove user
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/users/{user_id}'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_user_attribute(client):
    """Test case for remove_user_attribute

    Remove custom user attribute
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/users/{user_id}/userAttributes/{key}'.format(user_id=56, key='key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_emergency_mfa_code(client):
    """Test case for request_emergency_mfa_code

    Request emergency MFA code
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/users/{user_id}/mfa/emergency_code'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_last_admin_rooms_users(client):
    """Test case for request_last_admin_rooms_users

    Request rooms where the user is last admin
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/users/{user_id}/last_admin_rooms'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_user(client):
    """Test case for request_user

    Request user
    """
    params = [('effective_roles', True)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/users/{user_id}'.format(user_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_user_attributes(client):
    """Test case for request_user_attributes

    Request custom user attributes
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/users/{user_id}/userAttributes'.format(user_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_user_groups(client):
    """Test case for request_user_groups

    Request groups that user is a member of or / and can become a member
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/users/{user_id}/groups'.format(user_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_user_roles(client):
    """Test case for request_user_roles

    Request user's granted roles
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/users/{user_id}/roles'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_users(client):
    """Test case for request_users

    Request users
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example'),
                    ('sort', 'sort_example'),
                    ('include_attributes', True),
                    ('include_roles', True),
                    ('include_manageable_rooms', True)]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_users_rooms(client):
    """Test case for request_users_rooms

    Request rooms granted to the user or / and rooms that can be granted
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/users/{user_id}/rooms'.format(user_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_user_attributes(client):
    """Test case for set_user_attributes

    Set custom user attributes
    """
    body = {"items":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/users/{user_id}/userAttributes'.format(user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user(client):
    """Test case for update_user

    Update user's metadata
    """
    body = {"lastName":"lastName","gender":"n","receiverLanguage":"receiverLanguage","authData":{"method":"method","adConfigId":0,"login":"login","oidConfigId":6},"authMethods":[{"isEnabled":True,"options":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"authId":"authId"},{"isEnabled":True,"options":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"authId":"authId"}],"title":"title","userName":"userName","firstName":"firstName","lockStatus":1,"phone":"phone","mfaConfig":{"mfaEnforced":True},"isLocked":False,"expiration":{"enableExpiration":True,"expireAt":"2000-01-23T04:56:07.000+00:00"},"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/users/{user_id}'.format(user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user_attributes(client):
    """Test case for update_user_attributes

    Add or edit custom user attributes
    """
    body = {"items":[{"value":"value","key":"key"},{"value":"value","key":"key"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/users/{user_id}/userAttributes'.format(user_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

