# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_credentials import AccountCredentials
from openapi_server.models.api_error import ApiError
from openapi_server.models.change_role_request import ChangeRoleRequest
from openapi_server.models.complete_user_registration_request import CompleteUserRegistrationRequest
from openapi_server.models.organization_user_invitation_list_request import OrganizationUserInvitationListRequest
from openapi_server.models.paginated_response_of_organization import PaginatedResponseOfOrganization
from openapi_server.models.paginated_response_of_role import PaginatedResponseOfRole
from openapi_server.models.paginated_response_of_user_presentation import PaginatedResponseOfUserPresentation
from openapi_server.models.paginated_response_of_user_roles import PaginatedResponseOfUserRoles
from openapi_server.models.paginated_response_ofstring import PaginatedResponseOfstring
from openapi_server.models.password_reset_request import PasswordResetRequest
from openapi_server.models.password_reset_verification_request import PasswordResetVerificationRequest
from openapi_server.models.registration_verification_token_presentation import RegistrationVerificationTokenPresentation
from openapi_server.models.simple_message_response import SimpleMessageResponse
from openapi_server.models.user_presentation import UserPresentation
from openapi_server.models.user_registration_request import UserRegistrationRequest
from openapi_server.models.user_registration_response import UserRegistrationResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_user_roles(client):
    """Test case for add_user_roles

    Add role(s) to user
    """
    body = {"roles":["roles","roles"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/users/{username}/roles'.format(organization_id='organization_id_example', username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_complete_registration(client):
    """Test case for complete_registration

    Complete registration
    """
    body = {"password":"password","verificationToken":"verificationToken","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/account/registration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_user_by_username(client):
    """Test case for find_user_by_username

    Find by username
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_users(client):
    """Test case for find_users

    Find users
    """
    params = [('usernamePrefix', 'username_prefix_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_organization_roles(client):
    """Test case for get_all_organization_roles

    List users and their roles
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/roles'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organizations_of_user(client):
    """Test case for get_organizations_of_user

    Retrieve organizations of user
    """
    params = [('role', 'role_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/user/organizations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_roles(client):
    """Test case for get_user_roles

    Get user roles by username
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/users/{username}/roles'.format(organization_id='organization_id_example', username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_of_organization(client):
    """Test case for get_users_of_organization

    Find users in organization
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/users'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_invite_users(client):
    """Test case for invite_users

    Invite Users
    """
    body = {"invitations":[{"roles":["roles","roles"],"userName":"userName","email":"email"},{"roles":["roles","roles"],"userName":"userName","email":"email"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/users/invite'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_roles(client):
    """Test case for list_all_roles

    List roles
    """
    params = [('privilege', 'privilege_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/roles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_login(client):
    """Test case for login

    
    """
    body = {"password":"password","login":"login"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_register_user(client):
    """Test case for register_user

    Register user
    """
    body = {"password":"password","email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/account/registration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_remove_user_roles(client):
    """Test case for remove_user_roles

    Remove role(s) from user
    """
    body = {"roles":["roles","roles"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/users/{username}/roles'.format(organization_id='organization_id_example', username='username_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_request_password_reset(client):
    """Test case for request_password_reset

    Request password reset
    """
    body = {"username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/account/password',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_verify_password_reset(client):
    """Test case for verify_password_reset

    Verify password reset
    """
    body = {"password":"password","token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/account/password',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_verify_user_registration(client):
    """Test case for verify_user_registration

    Verify registration
    """
    body = {"token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/account/verification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

