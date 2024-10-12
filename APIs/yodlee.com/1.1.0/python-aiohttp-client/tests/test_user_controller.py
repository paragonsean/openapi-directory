# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_user_request import UpdateUserRequest
from openapi_server.models.user_access_tokens_response import UserAccessTokensResponse
from openapi_server.models.user_detail_response import UserDetailResponse
from openapi_server.models.user_request import UserRequest
from openapi_server.models.user_response import UserResponse
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_get_access_tokens(client):
    """Test case for get_access_tokens

    Get Access Tokens
    """
    params = [('appIds', 'app_ids_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/user/accessTokens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get User Details
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_user(client):
    """Test case for register_user

    Register User
    """
    body = {"user":{"preferences":{"dateFormat":"dateFormat","timeZone":"timeZone","currency":"AUD","locale":"en_US"},"address":{"zip":"zip","country":"country","address3":"address3","address2":"address2","city":"city","address1":"address1","state":"state"},"loginName":"loginName","name":{"middle":"middle","last":"last","fullName":"fullName","first":"first"},"email":"email","segmentName":"segmentName"}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/user/register',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saml_login(client):
    """Test case for saml_login

    Saml Login
    """
    params = [('issuer', 'issuer_example'),
                    ('samlResponse', 'saml_response_example'),
                    ('source', 'source_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/user/samlLogin',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unregister(client):
    """Test case for unregister

    Delete User
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/user/unregister',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user(client):
    """Test case for update_user

    Update User Details
    """
    body = {"user":{"preferences":{"dateFormat":"dateFormat","timeZone":"timeZone","currency":"AUD","locale":"en_US"},"address":{"zip":"zip","country":"country","address3":"address3","address2":"address2","city":"city","address1":"address1","state":"state"},"name":{"middle":"middle","last":"last","fullName":"fullName","first":"first"},"email":"email","segmentName":"segmentName"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_logout(client):
    """Test case for user_logout

    User Logout
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/user/logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

