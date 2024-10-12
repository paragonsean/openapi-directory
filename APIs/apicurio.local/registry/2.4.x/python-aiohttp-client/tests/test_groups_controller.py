# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_group_meta_data import CreateGroupMetaData
from openapi_server.models.error import Error
from openapi_server.models.group_meta_data import GroupMetaData
from openapi_server.models.group_search_results import GroupSearchResults
from openapi_server.models.sort_by import SortBy
from openapi_server.models.sort_order import SortOrder


pytestmark = pytest.mark.asyncio

async def test_create_group(client):
    """Test case for create_group

    Create a new group
    """
    body = {"description":"The description of the artifact.","id":"group-identifier","properties":{"custom-1":"foo","custom-2":"bar"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_group_by_id(client):
    """Test case for delete_group_by_id

    Delete a group by the specified ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_by_id(client):
    """Test case for get_group_by_id

    Get a group by the specified ID.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_groups(client):
    """Test case for list_groups

    List groups
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('order', openapi_server.SortOrder()),
                    ('orderby', openapi_server.SortBy())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

