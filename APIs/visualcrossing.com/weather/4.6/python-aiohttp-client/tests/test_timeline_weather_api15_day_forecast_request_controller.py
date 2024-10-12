# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_visual_crossing_web_services_rest_services_timeline_location_get(client):
    """Test case for visual_crossing_web_services_rest_services_timeline_location_get

    Historical and Forecast Weather API
    """
    params = [('contentType', 'json'),
                    ('unitGroup', 'us'),
                    ('include', 'days'),
                    ('lang', 'us'),
                    ('key', 'INSERT_YOUR_KEY')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/VisualCrossingWebServices/rest/services/timeline/{location}'.format(location='London,UK'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

