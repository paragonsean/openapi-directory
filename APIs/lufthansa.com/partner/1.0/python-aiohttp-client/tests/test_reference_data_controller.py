# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_seat_details(client):
    """Test case for seat_details

    Seat Details
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/seatdetails/{aircraft_code}/{cabin_code}'.format(aircraft_code='aircraft_code_example', cabin_code='C'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

