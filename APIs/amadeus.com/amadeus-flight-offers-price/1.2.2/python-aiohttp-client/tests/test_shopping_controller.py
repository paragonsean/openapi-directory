# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_price_query import GetPriceQuery
from openapi_server.models.success_pricing import SuccessPricing


pytestmark = pytest.mark.asyncio

async def test_quote_air_offers(client):
    """Test case for quote_air_offers

    Confirm pricing of given flightOffers.
    """
    price_flight_offers_body = openapi_server.GetPriceQuery()
    params = [('include', ['include_example']),
                    ('forceClass', False)]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
        'Content-Type': 'application/vnd.amadeus+json',
        'x_http_method_override': 'GET',
    }
    response = await client.request(
        method='POST',
        path='/v1/shopping/flight-offers/pricing',
        headers=headers,
        json=price_flight_offers_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

