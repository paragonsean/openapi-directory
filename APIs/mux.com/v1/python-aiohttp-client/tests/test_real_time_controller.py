# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_real_time_breakdown_response import GetRealTimeBreakdownResponse
from openapi_server.models.get_real_time_histogram_timeseries_response import GetRealTimeHistogramTimeseriesResponse
from openapi_server.models.get_real_time_timeseries_response import GetRealTimeTimeseriesResponse
from openapi_server.models.list_real_time_dimensions_response import ListRealTimeDimensionsResponse
from openapi_server.models.list_real_time_metrics_response import ListRealTimeMetricsResponse


pytestmark = pytest.mark.asyncio

async def test_get_realtime_breakdown(client):
    """Test case for get_realtime_breakdown

    Get Real-Time Breakdown
    """
    params = [('dimension', 'dimension_example'),
                    ('timestamp', 56),
                    ('filters[]', ['filters_example']),
                    ('order_by', 'order_by_example'),
                    ('order_direction', 'order_direction_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/realtime/metrics/{realtime_metric_id}/breakdown'.format(realtime_metric_id='current-concurrent-viewers'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_realtime_histogram_timeseries(client):
    """Test case for get_realtime_histogram_timeseries

    Get Real-Time Histogram Timeseries
    """
    params = [('filters[]', ['filters_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/realtime/metrics/{realtime_histogram_metric_id}/histogram-timeseries'.format(realtime_histogram_metric_id='video-startup-time'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_realtime_timeseries(client):
    """Test case for get_realtime_timeseries

    Get Real-Time Timeseries
    """
    params = [('filters[]', ['filters_example']),
                    ('timestamp', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/realtime/metrics/{realtime_metric_id}/timeseries'.format(realtime_metric_id='current-concurrent-viewers'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_realtime_dimensions(client):
    """Test case for list_realtime_dimensions

    List Real-Time Dimensions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/realtime/dimensions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_realtime_metrics(client):
    """Test case for list_realtime_metrics

    List Real-Time Metrics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/realtime/metrics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

