# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.channel_catalog_category_configuration_list import ChannelCatalogCategoryConfigurationList
from openapi_server.models.configure_category_request import ConfigureCategoryRequest


pytestmark = pytest.mark.asyncio

async def test_configure_channel_catalog_category(client):
    """Test case for configure_channel_catalog_category

    Configure channel catalog category
    """
    body = openapi_server.ConfigureCategoryRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/categories/configure'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_disable_channel_catalog_category_mapping(client):
    """Test case for disable_channel_catalog_category_mapping

    Disable a channel catalog category mapping
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/categories/disableMapping'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_categories(client):
    """Test case for get_channel_catalog_categories

    Get channel catalog categories
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/categories'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reenable_channel_catalog_category_mapping(client):
    """Test case for reenable_channel_catalog_category_mapping

    Reenable a channel catalog category mapping
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/categories/reenableMapping'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

