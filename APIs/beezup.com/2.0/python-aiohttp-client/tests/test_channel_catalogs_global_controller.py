# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_channel_catalog_request import AddChannelCatalogRequest
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.channel_catalog import ChannelCatalog
from openapi_server.models.channel_catalog_list import ChannelCatalogList
from openapi_server.models.filter_operator import FilterOperator
from openapi_server.models.links_get_channel_catalog_link import LinksGetChannelCatalogLink


pytestmark = pytest.mark.asyncio

async def test_add_channel_catalog(client):
    """Test case for add_channel_catalog

    Add a new channel catalog
    """
    body = openapi_server.AddChannelCatalogRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_channel_catalog(client):
    """Test case for delete_channel_catalog

    Delete the channel catalog
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user/channelCatalogs/{channel_catalog_id}'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog(client):
    """Test case for get_channel_catalog

    Get the channel catalog information
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channelCatalogs/{channel_catalog_id}'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_filter_operators(client):
    """Test case for get_channel_catalog_filter_operators

    Get channel catalog filter operators
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channelCatalogs/filterOperators',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalogs(client):
    """Test case for get_channel_catalogs

    List all your current channel catalogs
    """
    params = [('storeId', '04730364-9826-4ff3-92e4-51fccd02bf10')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channelCatalogs/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

