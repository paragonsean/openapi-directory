# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.success_booking import SuccessBooking


pytestmark = pytest.mark.asyncio

async def test_cancel_flight_order(client):
    """Test case for cancel_flight_order

    Cancel a given flight order
    """
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/booking/flight-orders/{flight_order_id}'.format(flight_order_id='flight_order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_flight_order(client):
    """Test case for get_flight_order

    Retrieve a given flight order
    """
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/booking/flight-orders/{flight_order_id}'.format(flight_order_id='flight_order_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

