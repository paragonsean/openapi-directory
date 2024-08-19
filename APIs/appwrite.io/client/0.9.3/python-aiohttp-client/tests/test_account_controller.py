# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_create_recovery_request import AccountCreateRecoveryRequest
from openapi_server.models.account_create_request import AccountCreateRequest
from openapi_server.models.account_create_verification_request import AccountCreateVerificationRequest
from openapi_server.models.account_update_email_request import AccountUpdateEmailRequest
from openapi_server.models.account_update_name_request import AccountUpdateNameRequest
from openapi_server.models.account_update_password_request import AccountUpdatePasswordRequest
from openapi_server.models.account_update_prefs_request import AccountUpdatePrefsRequest
from openapi_server.models.account_update_recovery_request import AccountUpdateRecoveryRequest
from openapi_server.models.account_update_verification_request import AccountUpdateVerificationRequest
from openapi_server.models.jwt import Jwt
from openapi_server.models.log_list import LogList
from openapi_server.models.session import Session
from openapi_server.models.session_list import SessionList
from openapi_server.models.token import Token
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_account_create(client):
    """Test case for account_create

    Create Account
    """
    body = openapi_server.AccountCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/account',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_create_anonymous_session(client):
    """Test case for account_create_anonymous_session

    Create Anonymous Session
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/account/sessions/anonymous',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_create_jwt(client):
    """Test case for account_create_jwt

    Create Account JWT
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/account/jwt',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_create_o_auth2_session(client):
    """Test case for account_create_o_auth2_session

    Create Account Session with OAuth2
    """
    params = [('success', 'https://appwrite.io/auth/oauth2/success'),
                    ('failure', 'https://appwrite.io/auth/oauth2/failure'),
                    ('scopes', [])]
    headers = { 
        'Project': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/account/sessions/oauth2/{provider}'.format(provider='provider_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_create_recovery(client):
    """Test case for account_create_recovery

    Create Password Recovery
    """
    body = openapi_server.AccountCreateRecoveryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/account/recovery',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_create_session(client):
    """Test case for account_create_session

    Create Account Session
    """
    body = openapi_server.AccountUpdateEmailRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/account/sessions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_create_verification(client):
    """Test case for account_create_verification

    Create Email Verification
    """
    body = openapi_server.AccountCreateVerificationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/account/verification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_delete(client):
    """Test case for account_delete

    Delete Account
    """
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_delete_session(client):
    """Test case for account_delete_session

    Delete Account Session
    """
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/account/sessions/{session_id}'.format(session_id='session_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_delete_sessions(client):
    """Test case for account_delete_sessions

    Delete All Account Sessions
    """
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/account/sessions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get(client):
    """Test case for account_get

    Get Account
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_logs(client):
    """Test case for account_get_logs

    Get Account Logs
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/account/logs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_prefs(client):
    """Test case for account_get_prefs

    Get Account Preferences
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/account/prefs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_session(client):
    """Test case for account_get_session

    Get Session By ID
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/account/sessions/{session_id}'.format(session_id='session_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_get_sessions(client):
    """Test case for account_get_sessions

    Get Account Sessions
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/account/sessions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_update_email(client):
    """Test case for account_update_email

    Update Account Email
    """
    body = openapi_server.AccountUpdateEmailRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/account/email',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_update_name(client):
    """Test case for account_update_name

    Update Account Name
    """
    body = openapi_server.AccountUpdateNameRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/account/name',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_update_password(client):
    """Test case for account_update_password

    Update Account Password
    """
    body = openapi_server.AccountUpdatePasswordRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/account/password',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_update_prefs(client):
    """Test case for account_update_prefs

    Update Account Preferences
    """
    body = openapi_server.AccountUpdatePrefsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/account/prefs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_update_recovery(client):
    """Test case for account_update_recovery

    Complete Password Recovery
    """
    body = openapi_server.AccountUpdateRecoveryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/account/recovery',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_update_verification(client):
    """Test case for account_update_verification

    Complete Email Verification
    """
    body = openapi_server.AccountUpdateVerificationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/account/verification',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

