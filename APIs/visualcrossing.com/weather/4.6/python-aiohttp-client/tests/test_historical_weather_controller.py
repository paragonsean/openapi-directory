# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_visual_crossing_web_services_rest_services_weatherdata_history_get(client):
    """Test case for visual_crossing_web_services_rest_services_weatherdata_history_get

    Retrieves hourly or daily historical weather records.
    """
    params = [('maxDistance', '-1'),
                    ('shortColumnNames', false),
                    ('endDateTime', '2020-02-04T00%3A00%3A00'),
                    ('aggregateHours', '24'),
                    ('collectStationContributions', false),
                    ('startDateTime', '2020-01-28T00%3A00%3A00'),
                    ('maxStations', '-1'),
                    ('allowAsynch', false),
                    ('locations', 'Sterling%2C%20VA%2C%20US'),
                    ('includeNormals', false),
                    ('contentType', 'json'),
                    ('unitGroup', 'us'),
                    ('key', 'INSERT_YOUR_KEY')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/VisualCrossingWebServices/rest/services/weatherdata/history',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

