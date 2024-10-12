# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.marketplace_channel_catalog_list import MarketplaceChannelCatalogList


pytestmark = pytest.mark.asyncio

async def test_get_marketplace_channel_catalogs(client):
    """Test case for get_marketplace_channel_catalogs

    Get your marketplace channel catalog list
    """
    params = [('storeId', '04730364-9826-4ff3-92e4-51fccd02bf10')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/channelcatalogs/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

