# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409
from openapi_server.models.inline_response412 import InlineResponse412
from openapi_server.models.invite_user_request import InviteUserRequest
from openapi_server.models.paged_user_response import PagedUserResponse
from openapi_server.models.password_request import PasswordRequest
from openapi_server.models.payee_type import PayeeType
from openapi_server.models.payee_user_self_update_request import PayeeUserSelfUpdateRequest
from openapi_server.models.register_sms_request import RegisterSmsRequest
from openapi_server.models.resend_token_request import ResendTokenRequest
from openapi_server.models.role_update_request import RoleUpdateRequest
from openapi_server.models.self_mfa_type_unregister_request import SelfMFATypeUnregisterRequest
from openapi_server.models.self_update_password_request import SelfUpdatePasswordRequest
from openapi_server.models.unregister_mfa_request import UnregisterMFARequest
from openapi_server.models.user_details_update_request import UserDetailsUpdateRequest
from openapi_server.models.user_response import UserResponse
from openapi_server.models.user_status import UserStatus
from openapi_server.models.user_type import UserType
from openapi_server.models.validate_password_response import ValidatePasswordResponse


pytestmark = pytest.mark.asyncio

async def test_delete_user_by_id_v2(client):
    """Test case for delete_user_by_id_v2

    Delete a User
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_user_v2(client):
    """Test case for disable_user_v2

    Disable a User
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/{user_id}/disable'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_user_v2(client):
    """Test case for enable_user_v2

    Enable a User
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/{user_id}/enable'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_self(client):
    """Test case for get_self

    Get Self
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/self',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_by_id_v2(client):
    """Test case for get_user_by_id_v2

    Get User
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invite_user(client):
    """Test case for invite_user

    Invite a User
    """
    body = {"email":"foo@example.com","entityId":"7fffa261-ac68-49e6-b605-d24a444d9206","firstName":"John","lastName":"Doe","mfaType":"TOTP","primaryContactNumber":"11235555555","roles":["velo.payor.admin"],"secondaryContactNumber":"11235555550","smsNumber":"11235555555","userType":"PAYEE","verificationCode":"123456"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/invite',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_users(client):
    """Test case for list_users

    List Users
    """
    params = [('type', openapi_server.UserType()),
                    ('status', openapi_server.UserStatus()),
                    ('entityId', 'entity_id_example'),
                    ('payeeType', openapi_server.PayeeType()),
                    ('page', 1),
                    ('pageSize', 25),
                    ('sort', 'email:asc')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_sms(client):
    """Test case for register_sms

    Register SMS Number
    """
    body = {"smsNumber":"11235555555"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/registration/sms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_token_0(client):
    """Test case for resend_token_0

    Resend a token
    """
    body = {"tokenType":"INVITE_MFA_USER","verificationCode":"123456"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/{user_id}/tokens'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_update(client):
    """Test case for role_update

    Update User Role
    """
    body = {"roles":["payor.admin"],"verificationCode":"123456"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/{user_id}/roleUpdate'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unlock_user_v2(client):
    """Test case for unlock_user_v2

    Unlock a User
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/{user_id}/unlock'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unregister_mfa(client):
    """Test case for unregister_mfa

    Unregister MFA for the user
    """
    body = {"mfaType":"TOTP","verificationCode":"123456"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/{user_id}/mfa/unregister'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unregister_mfa_for_self(client):
    """Test case for unregister_mfa_for_self

    Unregister MFA for Self
    """
    body = {"mfaType":"TOTP"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/self/mfa/unregister',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_password_self(client):
    """Test case for update_password_self

    Update Password for self
    """
    body = {"newPassword":"My_new_password","oldPassword":"My_current_password"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/self/password',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_details_update(client):
    """Test case for user_details_update

    Update User Details
    """
    body = {"email":"foo@example.com","firstName":"John","lastName":"Doe","mfaType":"TOTP","primaryContactNumber":"11235555555","secondaryContactNumber":"11235555550","smsNumber":"11235555555","verificationCode":"123456"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/{user_id}/userDetailsUpdate'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_details_update_for_self(client):
    """Test case for user_details_update_for_self

    Update User Details for self
    """
    body = {"email":"foo@example.com","firstName":"John","lastName":"Doe","primaryContactNumber":"11235555555","secondaryContactNumber":"11235555550","smsNumber":"11235555555"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/self/userDetailsUpdate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_password_self(client):
    """Test case for validate_password_self

    Validate the proposed password
    """
    body = {"password":"My_strong_password"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/users/self/password/validate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

