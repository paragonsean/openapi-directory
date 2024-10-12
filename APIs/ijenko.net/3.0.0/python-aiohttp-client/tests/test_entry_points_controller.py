# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_login import AuthLogin
from openapi_server.models.auth_tokens import AuthTokens
from openapi_server.models.default_error import DefaultError
from openapi_server.models.place_item import PlaceItem
from openapi_server.models.user_me import UserMe
from openapi_server.models.user_me_patch import UserMePatch


pytestmark = pytest.mark.asyncio

async def test_auth_account_login_0(client):
    """Test case for auth_account_login_0

    Get a token using login+password
    """
    login_info = {"password":"password","appId":"appId","login":"login","ttl":1800}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/auth/login',
        headers=headers,
        json=login_info,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_get(client):
    """Test case for me_get

    Information about the User
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_patch(client):
    """Test case for me_patch

    Update User information
    """
    user_patch = {"locale":"fr-FR"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/me',
        headers=headers,
        json=user_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_places(client):
    """Test case for me_places

    List accessible Places
    """
    params = [('embed-metadata', ['embed_metadata_example'])]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

