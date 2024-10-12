# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.success import Success


pytestmark = pytest.mark.asyncio

async def test_v2_successes_json_get(client):
    """Test case for v2_successes_json_get

    List successes
    """
    params = [('ids', [56]),
                    ('person_id', [56]),
                    ('updated_at', ['updated_at_example']),
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
        path='/v2/successes.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

