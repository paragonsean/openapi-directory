# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.group import Group


pytestmark = pytest.mark.asyncio

async def test_v2_groups_id_json_get(client):
    """Test case for v2_groups_id_json_get

    Fetch a group
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/groups/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_groups_json_get(client):
    """Test case for v2_groups_json_get

    List groups
    """
    params = [('ids', [56]),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/groups.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

