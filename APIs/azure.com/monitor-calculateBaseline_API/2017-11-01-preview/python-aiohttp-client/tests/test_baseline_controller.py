# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calculate_baseline_response import CalculateBaselineResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.time_series_information import TimeSeriesInformation


pytestmark = pytest.mark.asyncio

async def test_metric_baseline_calculate_baseline(client):
    """Test case for metric_baseline_calculate_baseline

    
    """
    time_series_information = {"timestamps":["2000-01-23T04:56:07.000+00:00","2000-01-23T04:56:07.000+00:00"],"values":[0.8008281904610115,0.8008281904610115],"sensitivities":["sensitivities","sensitivities"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{resource_uri}/providers/microsoft.insights/calculatebaseline'.format(resource_uri='resource_uri_example'),
        headers=headers,
        json=time_series_information,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

