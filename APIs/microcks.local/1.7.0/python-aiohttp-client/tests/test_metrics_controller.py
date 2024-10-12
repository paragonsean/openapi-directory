# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.daily_invocation_statistic import DailyInvocationStatistic
from openapi_server.models.test_conformance_metric import TestConformanceMetric
from openapi_server.models.test_result_summary import TestResultSummary
from openapi_server.models.weighted_metric_value import WeightedMetricValue


pytestmark = pytest.mark.asyncio

async def test_get_aggregated_invocations_stats(client):
    """Test case for get_aggregated_invocations_stats

    Get aggregated invocation statistics for a day
    """
    params = [('day', 'day_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/metrics/invocations/global',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_conformance_metrics_aggregation(client):
    """Test case for get_conformance_metrics_aggregation

    Get aggregation of conformance metrics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/metrics/conformance/aggregate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invocation_stats_by_service(client):
    """Test case for get_invocation_stats_by_service

    Get invocation statistics for Service
    """
    params = [('day', 'day_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/metrics/invocations/{service_name}/{service_version}'.format(service_name='service_name_example', service_version='service_version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_aggregated_invocations_stats(client):
    """Test case for get_latest_aggregated_invocations_stats

    Get aggregated invocations statistics for latest days
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/metrics/invocations/global/latest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_test_results(client):
    """Test case for get_latest_test_results

    Get latest tests results
    """
    params = [('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/metrics/tests/latest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_test_conformance_metric(client):
    """Test case for get_service_test_conformance_metric

    Get conformance metrics for a Service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/metrics/conformance/service/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_top_ivnocations_stats_by_day(client):
    """Test case for get_top_ivnocations_stats_by_day

    Get top invocation statistics for a day
    """
    params = [('day', 'day_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/metrics/invocations/top',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

