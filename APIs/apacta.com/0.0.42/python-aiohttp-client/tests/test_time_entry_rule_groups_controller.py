# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.time_entry_rule_groups_get200_response import TimeEntryRuleGroupsGet200Response


pytestmark = pytest.mark.asyncio

async def test_time_entry_rule_groups_get(client):
    """Test case for time_entry_rule_groups_get

    List time entry rule groups
    """
    params = [('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/time_entry_rule_groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

