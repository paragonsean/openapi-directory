# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.oauth_access_token_post200_response import OauthAccessTokenPost200Response
from openapi_server.models.oauth_access_token_post_request import OauthAccessTokenPostRequest
from openapi_server.models.oauth_live_session_token_post200_response import OauthLiveSessionTokenPost200Response
from openapi_server.models.oauth_live_session_token_post_request import OauthLiveSessionTokenPostRequest
from openapi_server.models.oauth_request_token_post200_response import OauthRequestTokenPost200Response
from openapi_server.models.oauth_request_token_post_request import OauthRequestTokenPostRequest


pytestmark = pytest.mark.asyncio

async def test_oauth_access_token_post(client):
    """Test case for oauth_access_token_post

    Obtain a access token
    """
    body = openapi_server.OauthAccessTokenPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tradingapi/v1/oauth/access_token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_live_session_token_post(client):
    """Test case for oauth_live_session_token_post

    Obtain a live session token
    """
    body = openapi_server.OauthLiveSessionTokenPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tradingapi/v1/oauth/live_session_token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_request_token_post(client):
    """Test case for oauth_request_token_post

    Obtain a request token
    """
    body = openapi_server.OauthRequestTokenPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tradingapi/v1/oauth/request_token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

