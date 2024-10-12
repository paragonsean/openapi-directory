# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.flight_order_query import FlightOrderQuery
from openapi_server.models.success_booking import SuccessBooking


pytestmark = pytest.mark.asyncio

async def test_create_fligt_orders(client):
    """Test case for create_fligt_orders

    Create Order associated to the Flight offers.
    """
    body = openapi_server.FlightOrderQuery()
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
        'Content-Type': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='POST',
        path='/v1/booking/flight-orders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

