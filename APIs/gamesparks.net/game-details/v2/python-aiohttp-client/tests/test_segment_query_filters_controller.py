# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.message_model import MessageModel
from openapi_server.models.segment_query_filter_config_model import SegmentQueryFilterConfigModel
from openapi_server.models.segment_query_filter_list_model import SegmentQueryFilterListModel


pytestmark = pytest.mark.asyncio

async def test_get_segment_query_filters_config_using_get(client):
    """Test case for get_segment_query_filters_config_using_get

    getSegmentQueryFiltersConfig
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/segmentQueryFilters/config'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_segment_query_filters_using_get(client):
    """Test case for get_segment_query_filters_using_get

    getSegmentQueryFilters
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/segmentQueryFilters'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_segment_query_standard_filters_using_get(client):
    """Test case for get_segment_query_standard_filters_using_get

    getSegmentQueryStandardFilters
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/admin/segmentQueryFilters/standardFilters'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_segment_query_filters_config_using_put(client):
    """Test case for update_segment_query_filters_config_using_put

    updateSegmentQueryFiltersConfig
    """
    body = {"hiddenFilters":["hiddenFilters","hiddenFilters"],"customFilters":[{"name":"name","options":["{}","{}"],"type":"type","key":"key"},{"name":"name","options":["{}","{}"],"type":"type","key":"key"}]}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/restv2/game/{api_key}/admin/segmentQueryFilters/config'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

