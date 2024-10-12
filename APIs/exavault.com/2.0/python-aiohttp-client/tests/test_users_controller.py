# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_user_request_body import AddUserRequestBody
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.update_user_request_body import UpdateUserRequestBody
from openapi_server.models.user_collection_response import UserCollectionResponse
from openapi_server.models.user_response import UserResponse


pytestmark = pytest.mark.asyncio

async def test_add_user(client):
    """Test case for add_user

    Create a user
    """
    body = {"homeResource":"/","password":"password","role":"user","permissions":{"modify":True,"notification":True,"download":True,"viewFormData":True,"upload":True,"share":True,"list":True,"delete":True,"changePassword":True,"deleteFormData":True},"nickname":"testnickname","onboarding":True,"timeZone":"America/Los_Angeles","welcomeEmail":True,"expiration":"2011-03-21 00:18:56","locked":True,"email":"testuser@example.com","username":"testuser"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Delete a user
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/users/{id}'.format(id=2224),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_by_id(client):
    """Test case for get_user_by_id

    Get info for a user
    """
    params = [('include', 'homeResource,owneraccount')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/users/{id}'.format(id=2224),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_users(client):
    """Test case for list_users

    Get a list of users
    """
    params = [('username', 'testuser'),
                    ('homeResource', 'home_resource_example'),
                    ('nickname', 'nickname_example'),
                    ('email', '*@example.co'),
                    ('role', 'use'),
                    ('status', 56),
                    ('search', 'search_example'),
                    ('offset', 50),
                    ('sort', 'homeDir,-modified'),
                    ('limit', 100),
                    ('include', 'homeResource,ownerAccount')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_user(client):
    """Test case for update_user

    Update a user
    """
    body = {"homeResource":"/","password":"password","role":"user","permissions":{"modify":True,"notification":True,"download":True,"viewFormData":True,"upload":True,"share":True,"list":True,"delete":True,"changePassword":True,"deleteFormData":True},"nickname":"testnickname","onboarding":True,"timeZone":"America/Los_Angeles","expiration":"2011-03-21 00:18:56","locked":True,"email":"testuser@example.com","username":"testuser"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/users/{id}'.format(id=2224),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

