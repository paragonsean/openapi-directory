# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.jwt import JWT
from openapi_server.models.jwt_data import JWTData
from openapi_server.models.jwt_error import JWTError
from openapi_server.models.refresh_json_web_token import RefreshJSONWebToken
from openapi_server.models.refresh_json_web_token_data import RefreshJSONWebTokenData
from openapi_server.models.refresh_json_web_token_error import RefreshJSONWebTokenError
from openapi_server.models.user import User
from openapi_server.models.user_data import UserData
from openapi_server.models.user_error import UserError
from openapi_server.models.verify_json_web_token import VerifyJSONWebToken
from openapi_server.models.verify_json_web_token_data import VerifyJSONWebTokenData
from openapi_server.models.verify_json_web_token_error import VerifyJSONWebTokenError


pytestmark = pytest.mark.asyncio

async def test_auth_jwt_token_auth(client):
    """Test case for auth_jwt_token_auth

    Create JSON Web Token (JWT)
    """
    jwt_data = {"password":"password","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/jwt-token-auth/',
        headers=headers,
        json=jwt_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_jwt_token_refresh(client):
    """Test case for auth_jwt_token_refresh

    Refresh a JSON Web Token (JWT)
    """
    refreshjwt_data = {"token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/jwt-token-refresh/',
        headers=headers,
        json=refreshjwt_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_jwt_token_verify(client):
    """Test case for auth_jwt_token_verify

    Validate JSON Web Token (JWT)
    """
    verifyjwt_data = {"token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/jwt-token-verify/',
        headers=headers,
        json=verifyjwt_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_register(client):
    """Test case for auth_register

    Register a user
    """
    user_data = {"password":"password","profile":{"timezone":"timezone","bio":"bio","company":"company","location":"location","avatar":"avatar","url":"url"},"last_name":"last_name","first_name":"first_name","email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/register/',
        headers=headers,
        json=user_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_login(client):
    """Test case for oauth_login

    
    """
    headers = { 
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/auth/login/{provider}'.format(provider='provider_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

