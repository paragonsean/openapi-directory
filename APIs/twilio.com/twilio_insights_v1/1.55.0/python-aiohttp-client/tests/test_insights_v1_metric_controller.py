# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_metric_response import ListMetricResponse
from openapi_server.models.metric_enum_stream_direction import MetricEnumStreamDirection
from openapi_server.models.metric_enum_twilio_edge import MetricEnumTwilioEdge


pytestmark = pytest.mark.asyncio

async def test_list_metric(client):
    """Test case for list_metric

    
    """
    params = [('Edge', openapi_server.MetricEnumTwilioEdge()),
                    ('Direction', openapi_server.MetricEnumStreamDirection()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Voice/{call_sid}/Metrics'.format(call_sid='call_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

