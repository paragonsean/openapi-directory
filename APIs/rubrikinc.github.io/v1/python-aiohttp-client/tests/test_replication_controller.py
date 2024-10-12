# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.disable_per_location_pause import DisablePerLocationPause
from openapi_server.models.enable_per_location_pause import EnablePerLocationPause


pytestmark = pytest.mark.asyncio

async def test_disable_per_location_pause(client):
    """Test case for disable_per_location_pause

    Resume replication from specified source clusters
    """
    body = {"sourceClusterUuids":["sourceClusterUuids","sourceClusterUuids"],"shouldSkipOldSnapshots":True}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/replication/location_pause/disable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_per_location_pause(client):
    """Test case for enable_per_location_pause

    Pause replication from specified source clusters
    """
    body = {"sourceClusterUuids":["sourceClusterUuids","sourceClusterUuids"],"shouldCancelImmediately":True}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/replication/location_pause/enable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

