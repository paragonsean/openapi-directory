# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token_credentials import AccessTokenCredentials
from openapi_server.models.client_credentials import ClientCredentials
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.public_authentication_output_model import PublicAuthenticationOutputModel


pytestmark = pytest.mark.asyncio

async def test_heart_beat_get_authorization(client):
    """Test case for heart_beat_get_authorization

    Returns http status code 204 for successful authentication.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/heartbeat/authorized',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_heart_beat_get_database_status(client):
    """Test case for heart_beat_get_database_status

    Can be used to check the status of the database.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/heartbeat/database',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_heart_beat_get_server_status(client):
    """Test case for heart_beat_get_server_status

    Can be used to check the status of the REST Api.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/heartbeat/server',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_bearer_authentication_get_access_token_json(client):
    """Test case for public_bearer_authentication_get_access_token_json

    Get oAuth2 access token.
    """
    body = {"refresh_token":"refresh_token","code":"code","grant_type":"client_credentials","scope":"scope","client_secret":"client_secret","redirect_uri":"redirect_uri","state":"state","client_id":"client_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/login/oauth/access_token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_bearer_authentication_get_access_token_token_from_refresh_token(client):
    """Test case for public_bearer_authentication_get_access_token_token_from_refresh_token

    Get new access token using a refresh token.
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/refreshtoken',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_bearer_authentication_get_authorization_code(client):
    """Test case for public_bearer_authentication_get_authorization_code

    Get the oAuth2 authorization code flow code.
    """
    params = [('response_type', 'response_type_example'),
                    ('state', 'state_example'),
                    ('client_id', 'client_id_example'),
                    ('redirect_uri', 'redirect_uri_example'),
                    ('scope', '')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/login/oauth/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_bearer_authentication_get_login_token(client):
    """Test case for public_bearer_authentication_get_login_token

    Can be used to get the login information and access token for the api client.
    """
    body = {"scope":"scope","client_secret":"client_secret","client_id":"client_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_bearer_authentication_logout(client):
    """Test case for public_bearer_authentication_logout

    Logout. Invalidates refresh token. Access token will be invalid when it expires.
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/signout',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

