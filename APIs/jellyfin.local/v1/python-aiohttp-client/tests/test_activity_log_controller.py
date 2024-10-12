# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_log_entry_query_result import ActivityLogEntryQueryResult


pytestmark = pytest.mark.asyncio

async def test_get_log_entries(client):
    """Test case for get_log_entries

    Gets activity log entries.
    """
    params = [('startIndex', 56),
                    ('limit', 56),
                    ('minDate', '2013-10-20T19:20:30+01:00'),
                    ('hasUserId', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/System/ActivityLog/Entries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

