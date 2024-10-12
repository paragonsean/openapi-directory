# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.login_request import LoginRequest
from openapi_server.models.login_response import LoginResponse
from openapi_server.models.radius_challenge_response import RadiusChallengeResponse
from openapi_server.models.recover_user_name_request import RecoverUserNameRequest
from openapi_server.models.reset_password400_response import ResetPassword400Response
from openapi_server.models.reset_password_request import ResetPasswordRequest
from openapi_server.models.reset_password_token_validate_response import ResetPasswordTokenValidateResponse
from openapi_server.models.reset_password_with_token_request import ResetPasswordWithTokenRequest


pytestmark = pytest.mark.asyncio

async def test_complete_open_id_login(client):
    """Test case for complete_open_id_login

    Complete OpenID Connect authentication
    """
    params = [('code', 'code_example'),
                    ('id_token', 'id_token_example'),
                    ('state', 'state_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/auth/openid/login',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_initiate_open_id_login(client):
    """Test case for initiate_open_id_login

    Initiate OpenID Connect authentication
    """
    params = [('issuer', 'issuer_example'),
                    ('redirect_uri', 'redirect_uri_example'),
                    ('language', 'language_example'),
                    ('test', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/auth/openid/login',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login(client):
    """Test case for login

    Authenticate user (Login)
    """
    body = {"password":"password","language":"language","state":"state","authType":"basic","login":"login","userName":"userName","token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/auth/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ping(client):
    """Test case for ping

    Ping
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/auth/ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recover_user_name(client):
    """Test case for recover_user_name

    Recover username
    """
    body = {"creatorLanguage":"creatorLanguage","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/auth/recover_username',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_password_reset(client):
    """Test case for request_password_reset

    Request password reset
    """
    body = {"creatorLanguage":"creatorLanguage","language":"language","login":"login","userName":"userName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/auth/reset_password',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_password(client):
    """Test case for reset_password

    Reset password
    """
    body = {"password":"password"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/auth/reset_password/{token}'.format(token='token_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_reset_password_token(client):
    """Test case for validate_reset_password_token

    Validate information for password reset
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/auth/reset_password/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

