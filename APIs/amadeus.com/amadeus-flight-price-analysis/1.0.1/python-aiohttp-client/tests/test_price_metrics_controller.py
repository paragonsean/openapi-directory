# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_itinerary_price_metrics200_response import GetItineraryPriceMetrics200Response


pytestmark = pytest.mark.asyncio

async def test_get_itinerary_price_metrics(client):
    """Test case for get_itinerary_price_metrics

    GET itinerary price metric
    """
    params = [('originIataCode', 'MAD'),
                    ('destinationIataCode', 'CDG'),
                    ('departureDate', '2021-03-21'),
                    ('currencyCode', 'EUR'),
                    ('oneWay', False)]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/analytics/itinerary-price-metrics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

