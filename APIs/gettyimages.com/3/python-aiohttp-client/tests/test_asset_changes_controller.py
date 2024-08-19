# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asset_changes import AssetChanges
from openapi_server.models.channel import Channel


pytestmark = pytest.mark.asyncio

async def test_v3_asset_changes_change_sets_change_set_id_delete(client):
    """Test case for v3_asset_changes_change_sets_change_set_id_delete

    Confirm asset change notifications.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/asset-changes/change-sets/{change_set_id}'.format(change_set_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_asset_changes_change_sets_put(client):
    """Test case for v3_asset_changes_change_sets_put

    Get asset change notifications.
    """
    params = [('channel_id', 56),
                    ('batch_size', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/asset-changes/change-sets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_asset_changes_channels_get(client):
    """Test case for v3_asset_changes_channels_get

    Get a list of asset change notification channels.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/asset-changes/channels',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

