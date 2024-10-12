# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.crm_user import CrmUser


pytestmark = pytest.mark.asyncio

async def test_v2_crm_users_json_get(client):
    """Test case for v2_crm_users_json_get

    List crm users
    """
    params = [('ids', [56]),
                    ('crm_id', ['crm_id_example']),
                    ('user_id', [56]),
                    ('user_guid', ['user_guid_example']),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('limit_paging_counts', True),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/crm_users.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

