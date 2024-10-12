# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.availability_response import AvailabilityResponse


pytestmark = pytest.mark.asyncio

async def test_availability_get(client):
    """Test case for availability_get

    Gets the availability and occupancy for a specific hotel and timespan.
    """
    params = [('hotelId', 56),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('expand', 'expand_example'),
                    ('skip', 56),
                    ('top', 56),
                    ('inlinecount', 'inlinecount_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/booking/v0/availability',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

