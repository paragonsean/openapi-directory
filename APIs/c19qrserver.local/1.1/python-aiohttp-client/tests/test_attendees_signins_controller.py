# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invalid_token import InvalidToken
from openapi_server.models.key_failure import KeyFailure
from openapi_server.models.signin import Signin
from openapi_server.models.signin_response import SigninResponse
from openapi_server.models.user_record import UserRecord


pytestmark = pytest.mark.asyncio

async def test_signin_post(client):
    """Test case for signin_post

    
    """
    body = openapi_server.Signin()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/signin',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_signin_signin_id_delete(client):
    """Test case for signin_signin_id_delete

    Delete a signin record
    """
    headers = { 
        'Accept': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/signin/{signin_id}'.format(signin_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_signin_signin_id_get(client):
    """Test case for signin_signin_id_get

    Retrieve the information associated with a signin record
    """
    headers = { 
        'Accept': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/signin/{signin_id}'.format(signin_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_signin_signin_id_put(client):
    """Test case for signin_signin_id_put

    Update a signin record
    """
    body = openapi_server.Signin()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/signin/{signin_id}'.format(signin_id=1),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_signins_get(client):
    """Test case for signins_get

    Get signin info
    """
    params = [('less_than', 56),
                    ('return_count', 100)]
    headers = { 
        'Accept': 'application/json',
        'TokenHeader': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/signins',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

