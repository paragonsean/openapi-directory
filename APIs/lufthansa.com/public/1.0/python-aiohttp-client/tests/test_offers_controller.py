# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_offers_lounges_by_location_get(client):
    """Test case for offers_lounges_by_location_get

    Lounges
    """
    params = [('cabinClass', 'cabin_class_example'),
                    ('tierCode', 'tier_code_example'),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/lounges/{location}'.format(location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offers_seatmaps_destination_date_cabin_class_by_flight_number_and_origin_get(client):
    """Test case for offers_seatmaps_destination_date_cabin_class_by_flight_number_and_origin_get

    Seat Maps
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/seatmaps/{flight_number}/{origin}/{destination}/{_date}/{cabin_class}'.format(flight_number='flight_number_example', origin='origin_example', destination='destination_example', _date='_date_example', cabin_class='cabin_class_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

