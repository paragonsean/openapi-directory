# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    Fetch a list of Users
    """
    params = [('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_delete(client):
    """Test case for users_id_delete

    Delete a User
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_id_put(client):
    """Test case for users_id_put

    Update a User
    """
    body = {"deviceReadonly":True,"poiLayer":"poiLayer","latitude":1.4658129805029452,"zoom":2,"coordinateFormat":"coordinateFormat","administrator":True,"password":"password","readonly":True,"phone":"phone","expirationTime":"2000-01-23T04:56:07.000+00:00","limitCommands":True,"twelveHourFormat":True,"name":"name","attributes":"{}","disabled":True,"id":6,"userLimit":5,"deviceLimit":0,"map":"map","email":"email","longitude":5.962133916683182}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/users/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_post(client):
    """Test case for users_post

    Create a User
    """
    body = {"deviceReadonly":True,"poiLayer":"poiLayer","latitude":1.4658129805029452,"zoom":2,"coordinateFormat":"coordinateFormat","administrator":True,"password":"password","readonly":True,"phone":"phone","expirationTime":"2000-01-23T04:56:07.000+00:00","limitCommands":True,"twelveHourFormat":True,"name":"name","attributes":"{}","disabled":True,"id":6,"userLimit":5,"deviceLimit":0,"map":"map","email":"email","longitude":5.962133916683182}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

