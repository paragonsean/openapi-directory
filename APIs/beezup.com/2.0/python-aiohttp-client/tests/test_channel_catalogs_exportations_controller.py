# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.channel_catalog_export_cache_info_response import ChannelCatalogExportCacheInfoResponse
from openapi_server.models.channel_catalog_exportation_history import ChannelCatalogExportationHistory


pytestmark = pytest.mark.asyncio

async def test_clear_channel_catalog_exportation_cache(client):
    """Test case for clear_channel_catalog_exportation_cache

    Clear the exportation cache
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/exportations/cache/clear'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_exportation_cache_info(client):
    """Test case for get_channel_catalog_exportation_cache_info

    Get the exportation cache information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/exportations/cache'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_exportation_history(client):
    """Test case for get_channel_catalog_exportation_history

    Get the exportation history
    """
    params = [('pageNumber', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/exportations/history'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

