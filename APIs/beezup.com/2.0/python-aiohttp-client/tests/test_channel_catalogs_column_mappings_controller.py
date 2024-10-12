# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.channel_catalog_column_mapping import ChannelCatalogColumnMapping


pytestmark = pytest.mark.asyncio

async def test_configure_channel_catalog_column_mappings(client):
    """Test case for configure_channel_catalog_column_mappings

    Configure channel catalog column mappings
    """
    body = [openapi_server.ChannelCatalogColumnMapping()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/columnMappings'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

