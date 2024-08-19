# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.source_collection_output import SourceCollectionOutput
from openapi_server.models.source_time_range_output import SourceTimeRangeOutput
from openapi_server.models.v1_models_source_source_output import V1ModelsSourceSourceOutput


pytestmark = pytest.mark.asyncio

async def test_get_all_sources_v1_source_ip_get(client):
    """Test case for get_all_sources_v1_source_ip_get

    Get the full information of all the source lists for the subscription level given.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/source/ip',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source_and_timerange_info_v1_source_ip_source_range_time_range_get(client):
    """Test case for get_source_and_timerange_info_v1_source_ip_source_range_time_range_get

    Get the information of the source list given for a specific time range.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/source/ip/{source}/range/{time_range}'.format(source='source_example', time_range='time_range_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_source_info_v1_source_ip_source_get(client):
    """Test case for get_source_info_v1_source_ip_source_get

    Get the full information of the source list given as argument.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/source/ip/{source}'.format(source='source_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

