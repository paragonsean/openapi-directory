# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hotel import Hotel


pytestmark = pytest.mark.asyncio

async def test_hotels_get_hotel(client):
    """Test case for hotels_get_hotel

    Get the details of the hotel with the speccified hotel id.
    """
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}'.format(hotel_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hotels_get_hotels(client):
    """Test case for hotels_get_hotels

    Get a list of all the hotels of a chain your application has access to.
    """
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

