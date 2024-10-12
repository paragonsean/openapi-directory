# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.room_type import RoomType


pytestmark = pytest.mark.asyncio

async def test_room_types_get_room_type(client):
    """Test case for room_types_get_room_type

    Get all the details for a specific room type in the hotel.
    """
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/room_types/{code}'.format(hotel_id=56, code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_room_types_get_room_types(client):
    """Test case for room_types_get_room_types

    Get a list with the details of all room types for for the specified hotel id.
    """
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/room_types'.format(hotel_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

