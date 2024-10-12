# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.obtain_token_request import ObtainTokenRequest
from openapi_server.models.obtain_token_response import ObtainTokenResponse
from openapi_server.models.renew_token_request import RenewTokenRequest
from openapi_server.models.renew_token_response import RenewTokenResponse
from openapi_server.models.revoke_token_request import RevokeTokenRequest
from openapi_server.models.revoke_token_response import RevokeTokenResponse


pytestmark = pytest.mark.asyncio

async def test_obtain_token(client):
    """Test case for obtain_token

    ObtainToken
    """
    body = {"request_body":{"client_id":"APPLICATION_ID","client_secret":"APPLICATION_SECRET","code":"CODE_FROM_AUTHORIZE","grant_type":"authorization_code"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/oauth2/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_renew_token(client):
    """Test case for renew_token

    RenewToken
    """
    body = {"request_body":{"access_token":"ACCESS_TOKEN"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'oauth2ClientSecret': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/oauth2/clients/{client_id}/access-token/renew'.format(client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_token(client):
    """Test case for revoke_token

    RevokeToken
    """
    body = {"request_body":{"access_token":"ACCESS_TOKEN","client_id":"CLIENT_ID"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'oauth2ClientSecret': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/oauth2/revoke',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

