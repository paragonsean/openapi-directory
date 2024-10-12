# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_metric_timeseries_data_response import GetMetricTimeseriesDataResponse
from openapi_server.models.get_overall_values_response import GetOverallValuesResponse
from openapi_server.models.list_all_metric_values_response import ListAllMetricValuesResponse
from openapi_server.models.list_breakdown_values_response import ListBreakdownValuesResponse
from openapi_server.models.list_insights_response import ListInsightsResponse


pytestmark = pytest.mark.asyncio

async def test_get_metric_timeseries_data(client):
    """Test case for get_metric_timeseries_data

    Get metric timeseries data
    """
    params = [('timeframe[]', ['timeframe_example']),
                    ('filters[]', ['filters_example']),
                    ('measurement', 'measurement_example'),
                    ('order_direction', 'order_direction_example'),
                    ('group_by', 'group_by_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/metrics/{metric_id}/timeseries'.format(metric_id='video_startup_time'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_overall_values(client):
    """Test case for get_overall_values

    Get Overall values
    """
    params = [('timeframe[]', ['timeframe_example']),
                    ('filters[]', ['filters_example']),
                    ('measurement', 'measurement_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/metrics/{metric_id}/overall'.format(metric_id='video_startup_time'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_all_metric_values(client):
    """Test case for list_all_metric_values

    List all metric values
    """
    params = [('timeframe[]', ['timeframe_example']),
                    ('filters[]', ['filters_example']),
                    ('dimension', 'dimension_example'),
                    ('value', 'value_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/metrics/comparison',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_breakdown_values(client):
    """Test case for list_breakdown_values

    List breakdown values
    """
    params = [('group_by', 'group_by_example'),
                    ('measurement', 'measurement_example'),
                    ('filters[]', ['filters_example']),
                    ('limit', 25),
                    ('page', 1),
                    ('order_by', 'order_by_example'),
                    ('order_direction', 'order_direction_example'),
                    ('timeframe[]', ['timeframe_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/metrics/{metric_id}/breakdown'.format(metric_id='video_startup_time'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_insights(client):
    """Test case for list_insights

    List Insights
    """
    params = [('measurement', 'measurement_example'),
                    ('order_direction', 'order_direction_example'),
                    ('timeframe[]', ['timeframe_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/metrics/{metric_id}/insights'.format(metric_id='video_startup_time'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

