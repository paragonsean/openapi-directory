# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.entire_detect_response import EntireDetectResponse
from openapi_server.models.last_detect_response import LastDetectResponse
from openapi_server.models.request import Request


pytestmark = pytest.mark.asyncio

async def test_entire_detect(client):
    """Test case for entire_detect

    Find anomalies for the entire series in batch.
    """
    body = {"period":1,"granularity":"yearly","maxAnomalyRatio":6.0274563,"series":[{"value":5.637377,"timestamp":"2000-01-23T04:56:07.000+00:00"},{"value":5.637377,"timestamp":"2000-01-23T04:56:07.000+00:00"}],"sensitivity":5,"customInterval":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/timeseries/entire/detect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_last_detect(client):
    """Test case for last_detect

    Detect anomaly status of the latest point in time series.
    """
    body = {"period":1,"granularity":"yearly","maxAnomalyRatio":6.0274563,"series":[{"value":5.637377,"timestamp":"2000-01-23T04:56:07.000+00:00"},{"value":5.637377,"timestamp":"2000-01-23T04:56:07.000+00:00"}],"sensitivity":5,"customInterval":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/timeseries/last/detect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

