# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_tier import AccountTier


pytestmark = pytest.mark.asyncio

async def test_v2_account_tiers_id_json_get(client):
    """Test case for v2_account_tiers_id_json_get

    Fetch an account tier
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/account_tiers/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_account_tiers_json_get(client):
    """Test case for v2_account_tiers_json_get

    List Account Tiers
    """
    params = [('ids', [56]),
                    ('name', ['name_example']),
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
        path='/v2/account_tiers.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

