# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.user import User
from openapi_server.models.user_collection import UserCollection
from openapi_server.models.user_collection_item import UserCollectionItem


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Delete a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/users/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users(client):
    """Test case for get_users

    List users
    """
    params = [('limit', 100),
                    ('offset', 56),
                    ('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_user(client):
    """Test case for patch_user

    Update a user
    """
    body = {"failed_login_count":0,"login_count":6,"password":"password","created_on":"created_on","last_login":"last_login","roles":[{"name":"name"},{"name":"name"}],"active":True,"last_name":"last_name","first_name":"first_name","changed_on":"changed_on","email":"email","username":"username"}
    params = [('update_mask', ['update_mask_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/users/{username}'.format(username='username_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_user(client):
    """Test case for post_user

    Create a user
    """
    body = {"failed_login_count":0,"login_count":6,"password":"password","created_on":"created_on","last_login":"last_login","roles":[{"name":"name"},{"name":"name"}],"active":True,"last_name":"last_name","first_name":"first_name","changed_on":"changed_on","email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

