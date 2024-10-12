# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.lti_credentials import LtiCredentials
from openapi_server.models.lti_credentials_creation import LtiCredentialsCreation
from openapi_server.models.organization_invitation import OrganizationInvitation
from openapi_server.models.organization_invitation_creation import OrganizationInvitationCreation
from openapi_server.models.user_admin_update import UserAdminUpdate
from openapi_server.models.user_creation import UserCreation
from openapi_server.models.user_details_admin import UserDetailsAdmin


pytestmark = pytest.mark.asyncio

async def test_count_orga_users(client):
    """Test case for count_orga_users

    Count the organization users using the provided filters
    """
    params = [('role', ['role_example']),
                    ('q', 'q_example'),
                    ('group', ['group_example']),
                    ('noActiveLicense', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/organizations/users/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_lti_credentials(client):
    """Test case for create_lti_credentials

    Create a new couple of LTI 1.x credentials
    """
    body = {"lms":"canvas","name":"My couple of credentials for Canvas"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/organizations/lti/credentials',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_invitation(client):
    """Test case for create_organization_invitation

    Create a new invitation to join the organization
    """
    body = {"email":"edu@flat.io","organizationRole":"teacher"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/organizations/invitations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_organization_user(client):
    """Test case for create_organization_user

    Create a new user account
    """
    body = {"firstname":"firstname","password":"password","locale":"en","email":"email","lastname":"lastname","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/organizations/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_lti_credentials(client):
    """Test case for list_lti_credentials

    List LTI 1.x credentials
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/organizations/lti/credentials',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_organization_invitations(client):
    """Test case for list_organization_invitations

    List the organization invitations
    """
    params = [('role', 'role_example'),
                    ('limit', 50),
                    ('next', 'next_example'),
                    ('previous', 'previous_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/organizations/invitations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_organization_users(client):
    """Test case for list_organization_users

    List the organization users
    """
    params = [('sort', ['sort_example']),
                    ('direction', 'direction_example'),
                    ('next', 'next_example'),
                    ('previous', 'previous_example'),
                    ('role', ['role_example']),
                    ('q', 'q_example'),
                    ('group', ['group_example']),
                    ('noActiveLicense', True),
                    ('licenseExpirationDate', ['license_expiration_date_example']),
                    ('onlyIds', True),
                    ('limit', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/organizations/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_organization_invitation(client):
    """Test case for remove_organization_invitation

    Remove an organization invitation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organizations/invitations/{invitation}'.format(invitation='invitation_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_organization_user(client):
    """Test case for remove_organization_user

    Remove an account from Flat
    """
    params = [('convertToIndividual', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organizations/users/{user}'.format(user='user_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_lti_credentials(client):
    """Test case for revoke_lti_credentials

    Revoke LTI 1.x credentials
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/organizations/lti/credentials/{credentials}'.format(credentials='credentials_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_user(client):
    """Test case for update_organization_user

    Update account information
    """
    body = {"firstname":"firstname","password":"password","organizationRole":"admin","email":"email","lastname":"lastname","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/organizations/users/{user}'.format(user='user_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

