# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage


pytestmark = pytest.mark.asyncio

async def test_disable_channel_catalog_product(client):
    """Test case for disable_channel_catalog_product

    Disable channel catalog product
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/products/{product_id}/disable'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0', product_id='578419df-1bbf-41a6-96fa-862e42182b67'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reenable_channel_catalog_product(client):
    """Test case for reenable_channel_catalog_product

    Reenable channel catalog product
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/products/{product_id}/reenable'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0', product_id='578419df-1bbf-41a6-96fa-862e42182b67'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

