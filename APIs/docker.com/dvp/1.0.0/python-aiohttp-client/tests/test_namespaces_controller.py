# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dataview_type import DataviewType
from openapi_server.models.response_data import ResponseData
from openapi_server.models.timespan_data import TimespanData
from openapi_server.models.timespan_model import TimespanModel
from openapi_server.models.timespan_type import TimespanType
from openapi_server.models.year_data import YearData


pytestmark = pytest.mark.asyncio

async def test_get_namespace_data_by_timespan(client):
    """Test case for get_namespace_data_by_timespan

    Get namespace data for timespan
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/publisher/analytics/v1/namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan}/{dataview}'.format(namespace='namespace_example', year=56, timespantype=openapi_server.TimespanType(), timespan=56, dataview=openapi_server.DataviewType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_namespace_timespan_metadata(client):
    """Test case for get_namespace_timespan_metadata

    Get namespace metadata for timespan
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/publisher/analytics/v1/namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan}'.format(namespace='namespace_example', year=56, timespantype=openapi_server.TimespanType(), timespan=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_namespace_timespans(client):
    """Test case for get_namespace_timespans

    Get timespans with data
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/publisher/analytics/v1/namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}'.format(namespace='namespace_example', year=56, timespantype=openapi_server.TimespanType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_namespace_years(client):
    """Test case for get_namespace_years

    Get years with data
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/publisher/analytics/v1/namespaces/{namespace}/pulls/exports/years'.format(namespace='namespace_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

