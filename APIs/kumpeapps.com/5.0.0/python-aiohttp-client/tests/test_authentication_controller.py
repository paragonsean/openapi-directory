# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response201 import InlineResponse201
from openapi_server.models.inline_response2011 import InlineResponse2011
from openapi_server.models.inline_response202 import InlineResponse202
from openapi_server.models.model403 import Model403
from openapi_server.models.model449 import Model449


pytestmark = pytest.mark.asyncio

async def test_appkey_patch(client):
    """Test case for appkey_patch

    Compromise app key
    """
    params = [('app_key', 'app_key_example'),
                    ('comments', 'comments_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v5/appkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appkey_post(client):
    """Test case for appkey_post

    Request app key
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example'),
                    ('supportsYubikey', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v5/appkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appkey_put(client):
    """Test case for appkey_put

    Deactivate app key
    """
    params = [('app_key', 'app_key_example')]
    headers = { 
        'Accept': 'application/json',
        'app_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v5/appkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_appkey_patch(client):
    """Test case for auth_appkey_patch

    Compromise app key
    """
    params = [('app_key', 'app_key_example'),
                    ('comments', 'comments_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v5/authentication/appkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_appkey_post(client):
    """Test case for auth_appkey_post

    Request app key
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example'),
                    ('supportsYubikey', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v5/authentication/appkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_appkey_put(client):
    """Test case for auth_appkey_put

    Deactivate app key
    """
    params = [('app_key', 'app_key_example')]
    headers = { 
        'Accept': 'application/json',
        'app_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v5/authentication/appkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_authkey_get(client):
    """Test case for auth_authkey_get

    Request auth key for user (login user)
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example'),
                    ('otp', 'otp_example'),
                    ('deviceName', 'device_name_example'),
                    ('identifierForVendor', 'identifier_for_vendor_example')]
    headers = { 
        'Accept': 'application/json',
        'app_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v5/authentication/authkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_authkey_patch(client):
    """Test case for auth_authkey_patch

    Compromise auth key
    """
    params = [('auth_key', 'auth_key_example'),
                    ('comments', 'comments_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v5/authentication/authkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_authkey_post(client):
    """Test case for auth_authkey_post

    Request auth key for user (login user)
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example'),
                    ('otp', 'otp_example')]
    headers = { 
        'Accept': 'application/json',
        'app_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v5/authentication/authkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_authkey_put(client):
    """Test case for auth_authkey_put

    Deactivate auth key (logout)
    """
    params = [('auth_key', 'auth_key_example')]
    headers = { 
        'Accept': 'application/json',
        'app_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v5/authentication/authkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_verifyotp_get(client):
    """Test case for auth_verifyotp_get

    Verifies YubiKey OTP for authenticated user
    """
    params = [('otp', 'otp_example')]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v5/authentication/verifyotp',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authkey_get(client):
    """Test case for authkey_get

    Request auth key for user (login user)
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example'),
                    ('otp', 'otp_example')]
    headers = { 
        'Accept': 'application/json',
        'app_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v5/authkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authkey_patch(client):
    """Test case for authkey_patch

    Compromise auth key
    """
    params = [('auth_key', 'auth_key_example'),
                    ('comments', 'comments_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v5/authkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authkey_post(client):
    """Test case for authkey_post

    Request auth key for user (login user)
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example'),
                    ('otp', 'otp_example')]
    headers = { 
        'Accept': 'application/json',
        'app_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v5/authkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authkey_put(client):
    """Test case for authkey_put

    Deactivate auth key (logout)
    """
    params = [('auth_key', 'auth_key_example')]
    headers = { 
        'Accept': 'application/json',
        'app_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v5/authkey',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

