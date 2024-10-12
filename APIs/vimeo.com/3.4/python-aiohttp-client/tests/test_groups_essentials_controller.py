# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_group_request import CreateGroupRequest
from openapi_server.models.group import Group
from openapi_server.models.legacy_error import LegacyError


pytestmark = pytest.mark.asyncio

async def test_create_group(client):
    """Test case for create_group

    Create a group
    """
    body = openapi_server.CreateGroupRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.group+json',
        'Content-Type': 'application/vnd.vimeo.group+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_group(client):
    """Test case for delete_group

    Delete a group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}'.format(group_id=1108),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group(client):
    """Test case for get_group

    Get a specific group
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.group+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}'.format(group_id=1108),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_groups(client):
    """Test case for get_groups

    Get all groups
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.group+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

