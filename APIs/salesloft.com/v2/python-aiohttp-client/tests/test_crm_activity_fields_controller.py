# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.crm_activity_field import CrmActivityField


pytestmark = pytest.mark.asyncio

async def test_v2_crm_activity_fields_json_get(client):
    """Test case for v2_crm_activity_fields_json_get

    List crm activity fields
    """
    params = [('source', 'source_example'),
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
        path='/v2/crm_activity_fields.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

