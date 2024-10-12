# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.flight_offers import FlightOffers
from openapi_server.models.seat_map_reply import SeatMapReply


pytestmark = pytest.mark.asyncio

async def test_get_seatmap_from_flight_offer(client):
    """Test case for get_seatmap_from_flight_offer

    Returns all the seat maps of a given flightOffer.
    """
    body = openapi_server.FlightOffers()
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
        'Content-Type': 'application/vnd.amadeus+json',
        'x_http_method_override': 'GET',
    }
    response = await client.request(
        method='POST',
        path='/v1/shopping/seatmaps',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_seatmap_from_order(client):
    """Test case for get_seatmap_from_order

    Returns all the seat maps of a given order.
    """
    params = [('flightOrderId', 'flight_order_id_example'),
                    ('flight-orderId', 'flight_order_id_example')]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/shopping/seatmaps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

