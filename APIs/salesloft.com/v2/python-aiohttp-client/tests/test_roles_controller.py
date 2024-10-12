# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_role import CustomRole


pytestmark = pytest.mark.asyncio

async def test_v2_custom_roles_id_json_get(client):
    """Test case for v2_custom_roles_id_json_get

    Fetch a custom role
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/custom_roles/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_custom_roles_json_get(client):
    """Test case for v2_custom_roles_json_get

    List custom roles
    """
    params = [('ids', ['ids_example']),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('limit_paging_counts', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/custom_roles.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

