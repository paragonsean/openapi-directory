# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_price_offers(client):
    """Test case for price_offers

    Price Offers
    """
    params = [('departureDate', 'departure_date_example'),
                    ('returnDate', 'return_date_example'),
                    ('service', 'amadeusBestPrice')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/promotions/priceoffers/flights/ond/{origin}/{destination}'.format(origin='origin_example', destination='destination_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

