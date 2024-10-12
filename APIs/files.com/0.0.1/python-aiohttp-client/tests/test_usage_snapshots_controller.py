# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.usage_snapshot_entity import UsageSnapshotEntity


pytestmark = pytest.mark.asyncio

async def test_get_usage_snapshots(client):
    """Test case for get_usage_snapshots

    List Usage Snapshots
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/usage_snapshots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

