# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.snapshot_storage_stats import SnapshotStorageStats


pytestmark = pytest.mark.asyncio

async def test_get_snapshot_storage_stats_v1(client):
    """Test case for get_snapshot_storage_stats_v1

    Returns storage stats for a snapshot
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/snapshot/{id}/storage/stats'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

