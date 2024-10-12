# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server.models.group_collection import GroupCollection
from openapi_server.models.group_definition import GroupDefinition


pytestmark = pytest.mark.asyncio

async def test_create_group(client):
    """Test case for create_group

    Create Group
    """
    body = {"displayName":"displayName","members":[{"type":"group","value":"value"},{"type":"group","value":"value"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/identity/v1/Groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_group(client):
    """Test case for delete_group

    Delete Group
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/identity/v1/Groups/{group_key}'.format(group_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group(client):
    """Test case for get_group

    Get Group
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/identity/v1/Groups/{group_key}'.format(group_key=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_groups(client):
    """Test case for get_groups

    Get Groups
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/identity/v1/Groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_group(client):
    """Test case for replace_group

    Replace Group
    """
    body = {"displayName":"displayName","members":[{"type":"group","value":"value"},{"type":"group","value":"value"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PUT',
        path='/identity/v1/Groups/{group_key}'.format(group_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_group(client):
    """Test case for update_group

    Update Group
    """
    body = {"displayName":"displayName","members":[{"type":"group","value":"value"},{"type":"group","value":"value"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PATCH',
        path='/identity/v1/Groups/{group_key}'.format(group_key=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

