# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.health import Health
from openapi_server.models.metric import Metric
from openapi_server.models.metrics_list import MetricsList


pytestmark = pytest.mark.asyncio

async def test_get_health(client):
    """Test case for get_health

    Get a summary of the application's health
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/system/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_metric(client):
    """Test case for get_metric

    Get the computed values of the specified metric
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/system/metrics/{metric_id}'.format(metric_id='metric_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_metrics(client):
    """Test case for get_metrics

    Get the identifiers and descriptions of the usage metrics
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/system/metrics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

