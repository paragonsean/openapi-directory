# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addons import Addons


pytestmark = pytest.mark.asyncio

async def test_addons_get(client):
    """Test case for addons_get

    Get a list of offers for addon services for the specified guest stay details.
    """
    params = [('hotelId', 56),
                    ('arrivalDate', '2013-10-20T19:20:30+01:00'),
                    ('departureDate', '2013-10-20T19:20:30+01:00'),
                    ('channelCode', 'channel_code_example'),
                    ('adults', 'adults_example'),
                    ('rooms', 'rooms_example'),
                    ('roomType', 'room_type_example'),
                    ('ratePlanCode', 'rate_plan_code_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/booking/v0/addons',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

