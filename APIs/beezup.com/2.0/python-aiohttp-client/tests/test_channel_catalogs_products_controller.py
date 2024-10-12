# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.beez_up_common_link3 import BeezUPCommonLink3
from openapi_server.models.channel_catalog_product_by_channel_catalog_request import ChannelCatalogProductByChannelCatalogRequest
from openapi_server.models.channel_catalog_product_by_channel_catalog_response import ChannelCatalogProductByChannelCatalogResponse
from openapi_server.models.channel_catalog_product_info import ChannelCatalogProductInfo
from openapi_server.models.channel_catalog_product_info_list import ChannelCatalogProductInfoList
from openapi_server.models.channel_catalog_products_counters import ChannelCatalogProductsCounters
from openapi_server.models.get_channel_catalog_product_info_list_request import GetChannelCatalogProductInfoListRequest


pytestmark = pytest.mark.asyncio

async def test_export_channel_catalog_product_info_list(client):
    """Test case for export_channel_catalog_product_info_list

    Export channel catalog product information list
    """
    body = openapi_server.GetChannelCatalogProductInfoListRequest()
    params = [('format', 'format_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/products/export'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_product_by_channel_catalog(client):
    """Test case for get_channel_catalog_product_by_channel_catalog

    Get channel catalog products related to these channel catalogs
    """
    body = openapi_server.ChannelCatalogProductByChannelCatalogRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/products',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_product_info(client):
    """Test case for get_channel_catalog_product_info

    Get channel catalog product information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/products/{product_id}'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0', product_id='578419df-1bbf-41a6-96fa-862e42182b67'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_product_info_list(client):
    """Test case for get_channel_catalog_product_info_list

    Get channel catalog product information list
    """
    body = openapi_server.GetChannelCatalogProductInfoListRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/products'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_products_counters(client):
    """Test case for get_channel_catalog_products_counters

    Get channel catalog products' counters
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/products/counters'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

