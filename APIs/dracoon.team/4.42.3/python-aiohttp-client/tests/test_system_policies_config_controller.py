# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.classification_policies_config import ClassificationPoliciesConfig
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.guest_users_policies_config import GuestUsersPoliciesConfig
from openapi_server.models.mfa_policies_config import MfaPoliciesConfig
from openapi_server.models.password_policies_config import PasswordPoliciesConfig
from openapi_server.models.update_classification_policies_config import UpdateClassificationPoliciesConfig
from openapi_server.models.update_guest_users_policies_config import UpdateGuestUsersPoliciesConfig
from openapi_server.models.update_mfa_policies_config import UpdateMfaPoliciesConfig
from openapi_server.models.update_password_policies_config import UpdatePasswordPoliciesConfig


pytestmark = pytest.mark.asyncio

async def test_change_classification_policies_config(client):
    """Test case for change_classification_policies_config

    Change classification policies
    """
    body = {"shareClassificationPolicies":{"classificationRequiresSharePassword":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/policies/classifications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_guest_users_policies_config(client):
    """Test case for change_guest_users_policies_config

    Change guest user policies
    """
    body = {"isInviteUsersEnabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/policies/guest_users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_mfa_policies_config(client):
    """Test case for change_mfa_policies_config

    Change MFA policies
    """
    body = {"isMfaEnforced":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/policies/mfa',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_password_policies_config(client):
    """Test case for change_password_policies_config

    Change password policies
    """
    body = {"encryptionPasswordPolicies":{"rejectKeyboardPatterns":True,"rejectUserInfo":True,"minLength":82,"characterRules":{"numberOfCharacteristicsToEnforce":0,"mustContainCharacters":["alpha","alpha"]}},"sharesPasswordPolicies":{"rejectKeyboardPatterns":True,"rejectUserInfo":True,"minLength":610,"rejectDictionaryWords":True,"characterRules":{"numberOfCharacteristicsToEnforce":0,"mustContainCharacters":["alpha","alpha"]}},"loginPasswordPolicies":{"passwordExpiration":{"enabled":True,"maxPasswordAge":5},"rejectKeyboardPatterns":True,"rejectUserInfo":True,"enforceLoginPasswordChange":False,"minLength":617,"rejectDictionaryWords":True,"userLockout":{"lockoutPeriod":2,"maxNumberOfLoginFailures":7,"enabled":True},"characterRules":{"numberOfCharacteristicsToEnforce":0,"mustContainCharacters":["alpha","alpha"]},"numberOfArchivedPasswords":2}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/policies/passwords',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enforce_login_password_change(client):
    """Test case for enforce_login_password_change

    Enforce login password change for all users
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/system/config/policies/passwords/enforce_change',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_classification_policies_config(client):
    """Test case for request_classification_policies_config

    Request classification policies
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/policies/classifications',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_guest_users_policies_config(client):
    """Test case for request_guest_users_policies_config

    Request guest user policies
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/policies/guest_users',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_mfa_policies_config(client):
    """Test case for request_mfa_policies_config

    Request MFA policies
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/policies/mfa',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_password_policies_config(client):
    """Test case for request_password_policies_config

    Request password policies
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/policies/passwords',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_password_policies_for_password_type(client):
    """Test case for request_password_policies_for_password_type

    Request password policies for a certain password type
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/policies/passwords/{password_type}'.format(password_type='password_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

