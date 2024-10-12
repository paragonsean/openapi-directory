# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.oauth_revoke_post_request import OauthRevokePostRequest
from openapi_server.models.oauth_token_post200_response import OauthTokenPost200Response
from openapi_server.models.oauth_token_post_request import OauthTokenPostRequest


pytestmark = pytest.mark.asyncio

async def test_oauth_authorize_get(client):
    """Test case for oauth_authorize_get

    
    """
    params = [('response_type', 'response_type_example'),
                    ('client_id', 'client_id_example'),
                    ('redirect_uri', 'redirect_uri_example'),
                    ('scope', 'scope_example'),
                    ('force_login', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/oauth/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_oauth_revoke_post(client):
    """Test case for oauth_revoke_post

    
    """
    body = openapi_server.OauthRevokePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
    }
    response = await client.request(
        method='POST',
        path='/oauth/revoke',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_oauth_token_post(client):
    """Test case for oauth_token_post

    
    """
    body = openapi_server.OauthTokenPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
    }
    response = await client.request(
        method='POST',
        path='/oauth/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

