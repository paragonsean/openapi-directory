# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.remote_bandwidth_snapshot_entity import RemoteBandwidthSnapshotEntity


pytestmark = pytest.mark.asyncio

async def test_get_remote_bandwidth_snapshots(client):
    """Test case for get_remote_bandwidth_snapshots

    List Remote Bandwidth Snapshots
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
        path='/api/rest/v1/remote_bandwidth_snapshots',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

