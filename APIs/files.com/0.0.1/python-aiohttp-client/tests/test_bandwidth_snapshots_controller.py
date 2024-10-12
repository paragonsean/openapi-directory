# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bandwidth_snapshot_entity import BandwidthSnapshotEntity


pytestmark = pytest.mark.asyncio

async def test_get_bandwidth_snapshots(client):
    """Test case for get_bandwidth_snapshots

    List Bandwidth Snapshots
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
        path='/api/rest/v1/bandwidth_snapshots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

