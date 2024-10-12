# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group import Group


pytestmark = pytest.mark.asyncio

async def test_groups_get(client):
    """Test case for groups_get

    Fetch a list of Groups
    """
    params = [('all', True),
                    ('userId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_id_delete(client):
    """Test case for groups_id_delete

    Delete a Group
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_id_put(client):
    """Test case for groups_id_put

    Update a Group
    """
    body = {"groupId":0,"name":"name","attributes":"{}","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_post(client):
    """Test case for groups_post

    Create a Group
    """
    body = {"groupId":0,"name":"name","attributes":"{}","id":6}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

