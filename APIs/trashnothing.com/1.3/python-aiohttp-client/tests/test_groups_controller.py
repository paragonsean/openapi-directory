# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server.models.search_groups200_response import SearchGroups200Response


pytestmark = pytest.mark.asyncio

async def test_get_group(client):
    """Test case for get_group

    Retrieve a group
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/groups/{group_id}'.format(group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_groups_by_ids(client):
    """Test case for get_groups_by_ids

    Retrieve multiple groups
    """
    params = [('group_ids', 'group_ids_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/groups/multiple',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_groups(client):
    """Test case for search_groups

    Search groups
    """
    params = [('name', 'name_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('distance', 100),
                    ('country', 'country_example'),
                    ('region', 'region_example'),
                    ('postal_code', 'postal_code_example'),
                    ('page', 1),
                    ('per_page', 20)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.3/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

