# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_user import AddUser
from openapi_server.models.add_user_response import AddUserResponse
from openapi_server.models.error import Error
from openapi_server.models.participation import Participation
from openapi_server.models.user import User
from openapi_server.models.user_participation_info import UserParticipationInfo
from openapi_server.models.user_with_permissions import UserWithPermissions


pytestmark = pytest.mark.asyncio

async def test_extparticipation_get(client):
    """Test case for extparticipation_get

    Gets a participation by external id
    """
    params = [('extid', 'extid_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/extparticipation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extuser_get(client):
    """Test case for extuser_get

    Gets a user by external id
    """
    params = [('extid', 'extid_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/extuser',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    Lists all users
    """
    params = [('limit', 5000),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_users_post(client):
    """Test case for users_post

    Adds a user
    """
    body = openapi_server.AddUser()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_userid_get(client):
    """Test case for users_userid_get

    User information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/users/{userid}'.format(userid='userid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_users_userid_patch(client):
    """Test case for users_userid_patch

    Updates user information
    """
    body = openapi_server.AddUser()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/users/{userid}'.format(userid='userid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_userid_pickey_apikeyget(client):
    """Test case for users_userid_pickey_apikeyget

    User profile picture
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/users/{userid}/pic?key={APIKEY}'.format(userid='userid_example', apikey='apikey_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_userid_project_participations_get(client):
    """Test case for users_userid_project_participations_get

    Returns information about the projects the user is a participant in.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/users/{userid}/projectParticipations'.format(userid='userid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

