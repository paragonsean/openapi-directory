# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_monitoring_breakdown_response import GetMonitoringBreakdownResponse
from openapi_server.models.get_monitoring_breakdown_timeseries_response import GetMonitoringBreakdownTimeseriesResponse
from openapi_server.models.get_monitoring_histogram_timeseries_response import GetMonitoringHistogramTimeseriesResponse
from openapi_server.models.get_monitoring_timeseries_response import GetMonitoringTimeseriesResponse
from openapi_server.models.list_monitoring_dimensions_response import ListMonitoringDimensionsResponse
from openapi_server.models.list_monitoring_metrics_response import ListMonitoringMetricsResponse


pytestmark = pytest.mark.asyncio

async def test_get_monitoring_breakdown(client):
    """Test case for get_monitoring_breakdown

    Get Monitoring Breakdown
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
        path='/data/v1/monitoring/metrics/{monitoring_metric_id}/breakdown'.format(monitoring_metric_id='current-concurrent-viewers'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_monitoring_breakdown_timeseries(client):
    """Test case for get_monitoring_breakdown_timeseries

    Get Monitoring Breakdown Timeseries
    """
    params = [('dimension', 'dimension_example'),
                    ('timeframe[]', ['timeframe_example']),
                    ('filters[]', ['filters_example']),
                    ('limit', 10),
                    ('order_by', 'order_by_example'),
                    ('order_direction', 'order_direction_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/monitoring/metrics/{monitoring_metric_id}/breakdown-timeseries'.format(monitoring_metric_id='current-concurrent-viewers'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_monitoring_histogram_timeseries(client):
    """Test case for get_monitoring_histogram_timeseries

    Get Monitoring Histogram Timeseries
    """
    params = [('filters[]', ['filters_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/monitoring/metrics/{monitoring_histogram_metric_id}/histogram-timeseries'.format(monitoring_histogram_metric_id='video-startup-time'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_monitoring_timeseries(client):
    """Test case for get_monitoring_timeseries

    Get Monitoring Timeseries
    """
    params = [('filters[]', ['filters_example']),
                    ('timestamp', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/monitoring/metrics/{monitoring_metric_id}/timeseries'.format(monitoring_metric_id='current-concurrent-viewers'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_monitoring_dimensions(client):
    """Test case for list_monitoring_dimensions

    List Monitoring Dimensions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/monitoring/dimensions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_monitoring_metrics(client):
    """Test case for list_monitoring_metrics

    List Monitoring Metrics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/monitoring/metrics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

