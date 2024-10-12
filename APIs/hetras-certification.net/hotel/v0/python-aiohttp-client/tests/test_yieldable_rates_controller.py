# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.yieldable_rate_time_slice import YieldableRateTimeSlice


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_yieldable_rates_save_prices(client):
    """Test case for yieldable_rates_save_prices

    Saves Yieldable Rate Prices for existing Yieldable Rateplan.
    """
    yieldable_rate_prices = {"date":"2000-01-23T04:56:07.000+00:00","rate_value":6.027456183070403,"number_of_persons":0,"room_type":"room_type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/hotel/v0/hotels/{hotel_id}/yieldable_rateplans/{rateplan_code}/$rates'.format(hotel_id=56, rateplan_code='rateplan_code_example'),
        headers=headers,
        json=yieldable_rate_prices,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

