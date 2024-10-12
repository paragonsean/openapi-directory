# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.frontline_v1_user import FrontlineV1User
from openapi_server.models.user_enum_state_type import UserEnumStateType


pytestmark = pytest.mark.asyncio

async def test_fetch_user(client):
    """Test case for fetch_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Users/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_user(client):
    """Test case for update_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'avatar': 'avatar_example',
        'friendly_name': 'friendly_name_example',
        'is_available': True,
        'state': openapi_server.UserEnumStateType()
        }
    response = await client.request(
        method='POST',
        path='/v1/Users/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

