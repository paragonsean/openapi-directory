# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.usage_daily_snapshot_entity import UsageDailySnapshotEntity


pytestmark = pytest.mark.asyncio

async def test_get_usage_daily_snapshots(client):
    """Test case for get_usage_daily_snapshots

    List Usage Daily Snapshots
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_gt', None),
                    ('filter_gteq', None),
                    ('filter_lt', None),
                    ('filter_lteq', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/usage_daily_snapshots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

