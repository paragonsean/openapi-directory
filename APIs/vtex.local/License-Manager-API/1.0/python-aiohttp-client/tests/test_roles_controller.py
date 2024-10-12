# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_user400_response import CreateUser400Response
from openapi_server.models.get_rolesby_user200_response_inner import GetRolesbyUser200ResponseInner
from openapi_server.models.get_user400_response import GetUser400Response
from openapi_server.models.list_roles_response import ListRolesResponse


pytestmark = pytest.mark.asyncio

async def test_get_list_roles(client):
    """Test case for get_list_roles

    Get List of Roles
    """
    params = [('numItems', 10),
                    ('pageNumber', 1),
                    ('sort', 'id'),
                    ('sortType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/license-manager/site/pvt/roles/list/paged',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rolesby_user(client):
    """Test case for get_rolesby_user

    Get Roles by User/appKey
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/license-manager/users/{user_id}/roles'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_rolesin_user(client):
    """Test case for put_rolesin_user

    Put Roles in User/appKey
    """
    body = [9000,9111,9333,9444]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/license-manager/users/{user_id}/roles'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_rolefrom_user(client):
    """Test case for remove_rolefrom_user

    Remove Role from User/appKey
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/license-manager/users/{user_id}/roles/{role_id}'.format(user_id='user_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

