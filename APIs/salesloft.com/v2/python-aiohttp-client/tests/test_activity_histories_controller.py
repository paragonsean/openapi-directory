# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_history import ActivityHistory


pytestmark = pytest.mark.asyncio

async def test_v2_activity_histories_get(client):
    """Test case for v2_activity_histories_get

    List Past Activities
    """
    params = [('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('type', 'type_example'),
                    ('_resource', 'resource_example'),
                    ('occurred_at', None),
                    ('pinned', True),
                    ('resource_type', 'resource_type_example'),
                    ('resource_id', ['resource_id_example']),
                    ('updated_at', None),
                    ('user_guid', 'user_guid_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/activity_histories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

