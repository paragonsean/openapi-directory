# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.exclusion_filter import ExclusionFilter
from openapi_server.models.exclusion_filters_response import ExclusionFiltersResponse


pytestmark = pytest.mark.asyncio

async def test_configure_channel_catalog_exclusion_filters(client):
    """Test case for configure_channel_catalog_exclusion_filters

    Configure channel catalog exclusion filters
    """
    body = [openapi_server.ExclusionFilter()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/exclusionFilters'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channel_catalog_exclusion_filters(client):
    """Test case for get_channel_catalog_exclusion_filters

    Get channel catalog exclusion filters
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/channelCatalogs/{channel_catalog_id}/exclusionFilters'.format(channel_catalog_id='6d6b04de-406b-4539-8e7e-bf3e8da5dfb0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

