# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth import Auth
from openapi_server.models.auth_error import AuthError
from openapi_server.models.client_auth_request import ClientAuthRequest
from openapi_server.models.convert_access_token_request import ConvertAccessTokenRequest
from openapi_server.models.error import Error
from openapi_server.models.exchange_auth_code_request import ExchangeAuthCodeRequest
from openapi_server.models.legacy_error import LegacyError


pytestmark = pytest.mark.asyncio

async def test_client_auth(client):
    """Test case for client_auth

    Authorize a client with OAuth
    """
    body = openapi_server.ClientAuthRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.auth+json',
        'Content-Type': 'application/vnd.vimeo.auth+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/oauth/authorize/client',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_access_token(client):
    """Test case for convert_access_token

    Convert OAuth 1 access tokens to OAuth 2 access tokens
    """
    body = openapi_server.ConvertAccessTokenRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.auth+json',
        'Content-Type': 'application/vnd.vimeo.auth+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/oauth/authorize/vimeo_oauth1',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_token(client):
    """Test case for delete_token

    Revoke the current access token
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.auth+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tokens',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_exchange_auth_code(client):
    """Test case for exchange_auth_code

    Exchange an authorization code for an access token
    """
    body = openapi_server.ExchangeAuthCodeRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.auth+json',
        'Content-Type': 'application/vnd.vimeo.auth+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/oauth/access_token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_token(client):
    """Test case for verify_token

    Verify an OAuth 2 token
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.auth+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/oauth/verify',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

