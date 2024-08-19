# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_user_payload import AddUserPayload
from openapi_server.models.delete_user_payload import DeleteUserPayload
from openapi_server.models.list_user_response import ListUserResponse
from openapi_server.models.user_teams_response import UserTeamsResponse
from openapi_server.models.v1_user import V1User


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_get(client):
    """Test case for api_public_v1_user_get

    List users
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_user_post(client):
    """Test case for api_public_v1_user_post

    Add a user
    """
    body = openapi_server.AddUserPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_user_user_delete(client):
    """Test case for api_public_v1_user_user_delete

    Remove a user
    """
    body = openapi_server.DeleteUserPayload()
    headers = { 
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api-public/v1/user/{user}'.format(user='user_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_get(client):
    """Test case for api_public_v1_user_user_get

    Retrieve information for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_user_user_put(client):
    """Test case for api_public_v1_user_user_put

    Update a user
    """
    body = openapi_server.AddUserPayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/api-public/v1/user/{user}'.format(user='user_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_teams_get(client):
    """Test case for api_public_v1_user_user_teams_get

    Retrieve the user's team membership
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}/teams'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

