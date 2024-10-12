# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.login_status import LoginStatus
from openapi_server.models.user_context import UserContext


pytestmark = pytest.mark.asyncio

async def test_get_qr_login(client):
    """Test case for get_qr_login

    Generate data for a login qr code
    """
    user_context = {"announceinfo":{"ip":"ip","useragent":"useragent","logo":"logo","info":"{}"},"sessioninfo":{"ip":"ip","useragent":"useragent","logo":"logo","info":"{}"}}
    params = [('img', 'img_example'),
                    ('s', 56)]
    headers = { 
        'Accept': 'application/octet-stream',
        'Content-Type': 'application/json',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/sessions/qr/login'.format(serverid='serverid_example'),
        headers=headers,
        json=user_context,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_session(client):
    """Test case for get_session

    Check if the user is logged in
    """
    headers = { 
        'Accept': 'application/json',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/sessions'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout(client):
    """Test case for logout

    Force a logout on the given session
    """
    headers = { 
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/sessions/logout'.format(serverid='serverid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provoke_login(client):
    """Test case for provoke_login

    Push a login confirmation to the user's app
    """
    user_context = {"announceinfo":{"ip":"ip","useragent":"useragent","logo":"logo","info":"{}"},"sessioninfo":{"ip":"ip","useragent":"useragent","logo":"logo","info":"{}"}}
    headers = { 
        'Content-Type': 'application/json',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/sessions/provokelogin'.format(serverid='serverid_example'),
        headers=headers,
        json=user_context,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_provoke_login_on_account(client):
    """Test case for provoke_login_on_account

    Push a login confirmation to the user's app
    """
    user_context = openapi_server.UserContext()
    headers = { 
        'Content-Type': 'application/json',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/accounts/{accountid}/provokelogin'.format(serverid='serverid_example', accountid=56),
        headers=headers,
        json=user_context,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provoke_login_on_user(client):
    """Test case for provoke_login_on_user

    Push a login confirmation to the user's app
    """
    user_context = {"announceinfo":{"ip":"ip","useragent":"useragent","logo":"logo","info":"{}"},"sessioninfo":{"ip":"ip","useragent":"useragent","logo":"logo","info":"{}"}}
    headers = { 
        'Content-Type': 'application/json',
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/users/{userid}/provokelogin'.format(serverid='serverid_example', userid='userid_example'),
        headers=headers,
        json=user_context,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

