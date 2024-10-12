# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.legacy_tracking_channel_catalog import LegacyTrackingChannelCatalog
from openapi_server.models.legacy_tracking_channel_catalog_list import LegacyTrackingChannelCatalogList


pytestmark = pytest.mark.asyncio

async def test_get_legacy_tracking_channel_catalog(client):
    """Test case for get_legacy_tracking_channel_catalog

    Get the channel catalog configured to use legacy tracking format information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/legacyTracking/channelCatalogs/{channel_catalog_id}'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_legacy_tracking_channel_catalogs(client):
    """Test case for get_legacy_tracking_channel_catalogs

    List all your current channel catalogs configured to use legacy tracking format
    """
    params = [('storeId', '04730364-9826-4ff3-92e4-51fccd02bf10')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/legacyTracking/channelCatalogs/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_migrate_legacy_tracking_channel_catalog(client):
    """Test case for migrate_legacy_tracking_channel_catalog

    Migrate a channel catalog to current tracking format
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/legacyTracking/channelCatalogs/{channel_catalog_id}/migrate'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

