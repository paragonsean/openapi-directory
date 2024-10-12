# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certs import Certs
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.open_id_configuration import OpenIdConfiguration
from openapi_server.models.session_request import SessionRequest
from openapi_server.models.session_response import SessionResponse


pytestmark = pytest.mark.asyncio

async def test_v05_certs_get(client):
    """Test case for v05_certs_get

    Get certs for JWT verification
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/gateway/v0.5/certs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v05_sessions_post(client):
    """Test case for v05_sessions_post

    Get access token
    """
    body = {"clientId":"clientId","clientSecret":"clientSecret","grantType":"client_credentials","refreshToken":"refreshToken"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/gateway/v0.5/sessions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v05_well_known_openid_configuration_get(client):
    """Test case for v05_well_known_openid_configuration_get

    Get openid configuration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/gateway/v0.5/.well-known/openid-configuration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

