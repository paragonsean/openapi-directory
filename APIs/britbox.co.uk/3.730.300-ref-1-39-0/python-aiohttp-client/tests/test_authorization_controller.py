# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.account_token_by_code_request import AccountTokenByCodeRequest
from openapi_server.models.account_token_request import AccountTokenRequest
from openapi_server.models.device_authorization_code import DeviceAuthorizationCode
from openapi_server.models.device_registration_request import DeviceRegistrationRequest
from openapi_server.models.profile_token_request import ProfileTokenRequest
from openapi_server.models.service_error import ServiceError
from openapi_server.models.single_sign_on_request import SingleSignOnRequest
from openapi_server.models.token_refresh_request import TokenRefreshRequest


pytestmark = pytest.mark.asyncio

async def test_generate_device_authorization_code(client):
    """Test case for generate_device_authorization_code

    
    """
    body = {"name":"name","id":"id","type":"type"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/authorization/device/code',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_token(client):
    """Test case for get_account_token

    
    """
    body = {"email":"","password":"","scopes":["Catalog"]}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/authorization',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_token_by_code(client):
    """Test case for get_account_token_by_code

    
    """
    body = {"code":"code","id":"id","scopes":["Catalog","Catalog"]}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/authorization/device',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile_token(client):
    """Test case for get_profile_token

    
    """
    body = {"pin":"pin","profileId":"profileId","cookieType":"Session","scopes":["Catalog","Catalog"]}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/authorization/profile',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refresh_token(client):
    """Test case for refresh_token

    
    """
    body = {"cookieType":"Session","token":"token"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/authorization/refresh',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sign_out(client):
    """Test case for sign_out

    
    """
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/authorization',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_single_sign_on(client):
    """Test case for single_sign_on

    
    """
    body = {"linkAccounts":True,"provider":"Facebook","cookieType":"Session","scopes":["Catalog","Catalog"],"token":"token"}
    params = [('ff', ['ff_example']),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/authorization/sso',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

