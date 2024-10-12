# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authentiq_id import AuthentiqID
from openapi_server.models.claims import Claims
from openapi_server.models.error import Error
from openapi_server.models.key_bind200_response import KeyBind200Response
from openapi_server.models.key_register201_response import KeyRegister201Response
from openapi_server.models.push_login_request200_response import PushLoginRequest200Response
from openapi_server.models.push_token import PushToken
from openapi_server.models.sign_request201_response import SignRequest201Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/jwt not supported by Connexion")
async def test_key_register_0(client):
    """Test case for key_register_0

    
    """
    body = openapi_server.AuthentiqID()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/jwt',
    }
    response = await client.request(
        method='POST',
        path='/key',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/jwt not supported by Connexion")
async def test_key_update_0(client):
    """Test case for key_update_0

    
    """
    body = openapi_server.AuthentiqID()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/jwt',
    }
    response = await client.request(
        method='POST',
        path='/key/{pk}'.format(pk='pk_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/jwt not supported by Connexion")
async def test_push_login_request_0(client):
    """Test case for push_login_request_0

    
    """
    body = openapi_server.PushToken()
    params = [('callback', 'param_callback_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/jwt',
    }
    response = await client.request(
        method='POST',
        path='/login',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sign_confirm_0(client):
    """Test case for sign_confirm_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/scope/{job}'.format(job='job_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/jwt not supported by Connexion")
async def test_sign_request_0(client):
    """Test case for sign_request_0

    
    """
    body = openapi_server.Claims()
    params = [('test', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/jwt',
    }
    response = await client.request(
        method='POST',
        path='/scope',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

