# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_visual_crossing_web_services_rest_services_weatherdata_forecast_get(client):
    """Test case for visual_crossing_web_services_rest_services_weatherdata_forecast_get

    Weather Forecast API
    """
    params = [('sendAsDatasource', false),
                    ('allowAsynch', false),
                    ('shortColumnNames', false),
                    ('locations', 'Sterling%2C%20VA%2C%20US'),
                    ('aggregateHours', '24'),
                    ('contentType', 'json'),
                    ('unitGroup', 'us'),
                    ('key', 'INSERT_YOUR_KEY')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/VisualCrossingWebServices/rest/services/weatherdata/forecast',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

