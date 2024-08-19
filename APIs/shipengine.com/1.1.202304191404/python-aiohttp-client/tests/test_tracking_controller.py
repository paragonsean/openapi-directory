# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_tracking_log_response_body import GetTrackingLogResponseBody


pytestmark = pytest.mark.asyncio

async def test_get_tracking_log(client):
    """Test case for get_tracking_log

    Get Tracking Information
    """
    params = [('carrier_code', 'stamps_com'),
                    ('tracking_number', '9405511899223197428490')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/tracking',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_tracking(client):
    """Test case for start_tracking

    Start Tracking a Package
    """
    params = [('carrier_code', 'stamps_com'),
                    ('tracking_number', '9405511899223197428490')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/tracking/start',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_tracking(client):
    """Test case for stop_tracking

    Stop Tracking a Package
    """
    params = [('carrier_code', 'stamps_com'),
                    ('tracking_number', '9405511899223197428490')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/tracking/stop',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

