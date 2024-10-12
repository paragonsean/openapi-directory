# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sales_channelby_id200_response import SalesChannelbyId200Response


pytestmark = pytest.mark.asyncio

async def test_sales_channel_list(client):
    """Test case for sales_channel_list

    Get Sales Channel List
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pvt/saleschannel/list',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_channelby_id(client):
    """Test case for sales_channelby_id

    Get Sales Channel by ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/saleschannel/{sales_channel_id}'.format(sales_channel_id='1'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

