# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.o_auth2_error import OAuth2Error
from openapi_server.models.token import Token
from openapi_server.models.user_info import UserInfo


pytestmark = pytest.mark.asyncio

async def test_authorize(client):
    """Test case for authorize

    Authenticate a user
    """
    params = [('client_id', 'client_id_example'),
                    ('response_type', 'response_type_example'),
                    ('scope', 'scope_example'),
                    ('redirect_uri', 'redirect_uri_example'),
                    ('state', 'state_example'),
                    ('response_mode', 'response_mode_example'),
                    ('nonce', 'nonce_example'),
                    ('display', 'page'),
                    ('prompt', 'login'),
                    ('max_age', 0),
                    ('ui_locales', 'ui_locales_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_token(client):
    """Test case for token

    Obtain an ID Token
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'authorization': 'authorization_example',
    }
    data = {
        'client_id': 'client_id_example',
        'client_secret': 'client_secret_example',
        'code': 'code_example',
        'grant_type': 'grant_type_example',
        'redirect_uri': 'redirect_uri_example'
        }
    response = await client.request(
        method='POST',
        path='/token',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_info(client):
    """Test case for user_info

    Retrieve a user profile
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/userinfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

