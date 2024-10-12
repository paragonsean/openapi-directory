# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_flight_offers_query import GetFlightOffersQuery
from openapi_server.models.success import Success
from openapi_server.models.success1 import Success1


pytestmark = pytest.mark.asyncio

async def test_get_flight_offers(client):
    """Test case for get_flight_offers

    Return list of Flight Offers based on searching criteria.
    """
    params = [('originLocationCode', 'SYD'),
                    ('destinationLocationCode', 'BKK'),
                    ('departureDate', '2021-02-01'),
                    ('returnDate', '2013-10-20'),
                    ('adults', 1),
                    ('children', 56),
                    ('infants', 56),
                    ('travelClass', 'travel_class_example'),
                    ('includedAirlineCodes', 'included_airline_codes_example'),
                    ('excludedAirlineCodes', 'excluded_airline_codes_example'),
                    ('nonStop', False),
                    ('currencyCode', 'currency_code_example'),
                    ('maxPrice', 56),
                    ('max', 250)]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/shopping/flight-offers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_flight_offers(client):
    """Test case for search_flight_offers

    Return list of Flight Offers based on posted searching criteria.
    """
    body = openapi_server.GetFlightOffersQuery()
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
        'Content-Type': 'application/vnd.amadeus+json',
        'x_http_method_override': 'GET',
    }
    response = await client.request(
        method='POST',
        path='/v2/shopping/flight-offers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

