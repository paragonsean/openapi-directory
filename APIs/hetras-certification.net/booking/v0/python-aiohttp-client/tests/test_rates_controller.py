# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rates import Rates


pytestmark = pytest.mark.asyncio

async def test_rates_get(client):
    """Test case for rates_get

    Get a list of room offers for the specified guest stay details.
    """
    params = [('hotelId', 56),
                    ('arrivalDate', '2013-10-20T19:20:30+01:00'),
                    ('departureDate', '2013-10-20T19:20:30+01:00'),
                    ('channelCode', 'channel_code_example'),
                    ('adults', 'adults_example'),
                    ('rooms', 'rooms_example'),
                    ('roomType', 'room_type_example'),
                    ('ratePlanCode', 'rate_plan_code_example'),
                    ('groupCode', 'group_code_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/booking/v0/rates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

