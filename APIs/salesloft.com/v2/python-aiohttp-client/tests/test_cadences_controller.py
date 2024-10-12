# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cadence import Cadence


pytestmark = pytest.mark.asyncio

async def test_v2_cadences_id_json_get(client):
    """Test case for v2_cadences_id_json_get

    Fetch a cadence
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/cadences/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_cadences_json_get(client):
    """Test case for v2_cadences_json_get

    List cadences
    """
    params = [('ids', [56]),
                    ('updated_at', ['updated_at_example']),
                    ('team_cadence', True),
                    ('shared', True),
                    ('owned_by_guid', ['owned_by_guid_example']),
                    ('people_addable', True),
                    ('name', ['name_example']),
                    ('group_ids', 'group_ids_example'),
                    ('archived', True),
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
        path='/v2/cadences.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

