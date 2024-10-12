# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.channel_catalog_marketplace_properties import ChannelCatalogMarketplaceProperties
from openapi_server.models.channel_catalog_marketplace_settings import ChannelCatalogMarketplaceSettings
from openapi_server.models.set_channel_catalog_marketplace_settings_request import SetChannelCatalogMarketplaceSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_marketplace_properties(client):
    """Test case for get_channel_catalog_marketplace_properties

    Get the marketplace properties for a channel catalog
    """
    params = [('redirectionPageUrl', 'redirection_page_url_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': ['accept_language_example'],
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/channelcatalogs/{channel_catalog_id}/properties'.format(channel_catalog_id='channel_catalog_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_marketplace_settings(client):
    """Test case for get_channel_catalog_marketplace_settings

    Get the marketplace settings for a channel catalog
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/channelcatalogs/{channel_catalog_id}/settings'.format(channel_catalog_id='channel_catalog_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_channel_catalog_marketplace_settings(client):
    """Test case for set_channel_catalog_marketplace_settings

    Save new marketplace settings for a channel catalog
    """
    body = openapi_server.SetChannelCatalogMarketplaceSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/channelcatalogs/{channel_catalog_id}/settings'.format(channel_catalog_id='channel_catalog_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

