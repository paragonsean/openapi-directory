# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.daily_rates_response import DailyRatesResponse


pytestmark = pytest.mark.asyncio

async def test_daily_rates_get_daily_rates(client):
    """Test case for daily_rates_get_daily_rates

    Get a list of daily rates given a hotel Id, a channel code and a date range.
    """
    params = [('hotelId', 56),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('channelCode', 'channel_code_example'),
                    ('expand', ['expand_example']),
                    ('ratePlanCodes', ['rate_plan_codes_example']),
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
        path='/api/booking/v0/daily_rates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

