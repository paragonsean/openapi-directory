# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.booking_schema import BookingSchema
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hotel_booked_response import HotelBookedResponse


pytestmark = pytest.mark.asyncio

async def test_create_booking(client):
    """Test case for create_booking

    Create Orders associated to the Hotel Offers
    """
    request_body = openapi_server.BookingSchema()
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
        'Content-Type': 'application/vnd.amadeus+json',
        'ama_client_ref': 'ama_client_ref_example',
        'accept_encoding': 'accept_encoding_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/booking/hotel-bookings',
        headers=headers,
        json=request_body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

