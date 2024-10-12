# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.log_analytics_operation_result import LogAnalyticsOperationResult
from openapi_server.models.request_rate_by_interval_input import RequestRateByIntervalInput
from openapi_server.models.throttled_requests_input import ThrottledRequestsInput


pytestmark = pytest.mark.asyncio

async def test_log_analytics_export_request_rate_by_interval(client):
    """Test case for log_analytics_export_request_rate_by_interval

    
    """
    parameters = {"intervalLength":"ThreeMins"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/{location}/logAnalytics/apiAccess/getRequestRateByInterval'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_log_analytics_export_throttled_requests(client):
    """Test case for log_analytics_export_throttled_requests

    
    """
    parameters = {"groupByResourceName":True,"groupByOperationName":True,"groupByThrottlePolicy":True,"fromTime":"2000-01-23T04:56:07.000+00:00","blobContainerSasUri":"blobContainerSasUri","toTime":"2000-01-23T04:56:07.000+00:00"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Compute/locations/{location}/logAnalytics/apiAccess/getThrottledRequests'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

