# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credentials import Credentials
from openapi_server.models.user import User
from openapi_server.models.user_token import UserToken


pytestmark = pytest.mark.asyncio

async def test_get_basic_user_information(client):
    """Test case for get_basic_user_information

    Get Basic User Information
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/auth/{token}/basicuserinformation'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_in(client):
    """Test case for log_in

    Log In
    """
    body = {"password":"password","apiKey":"apiKey","username":"username"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/login',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_out(client):
    """Test case for log_out

    Log Out
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/auth/logout/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

