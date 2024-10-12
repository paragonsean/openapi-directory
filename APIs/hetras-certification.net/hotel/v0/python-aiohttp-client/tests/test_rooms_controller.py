# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_room_patch_request import OperationRoomPatchRequest
from openapi_server.models.room import Room
from openapi_server.models.room_list_response import RoomListResponse
from openapi_server.models.total_count_response import TotalCountResponse


pytestmark = pytest.mark.asyncio

async def test_rooms_get_available_rooms(client):
    """Test case for rooms_get_available_rooms

    Request available rooms using a given criteria.
    """
    params = [('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('adults', 'adults_example'),
                    ('includeOutOfService', True),
                    ('roomTypes', ['room_types_example']),
                    ('amenities', ['amenities_example']),
                    ('views', ['views_example']),
                    ('locations', ['locations_example']),
                    ('skip', 56),
                    ('top', 56),
                    ('inlinecount', 'inlinecount_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/rooms/available'.format(hotel_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rooms_get_room(client):
    """Test case for rooms_get_room

    Get all the details for a specific room in the hotel.
    """
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/rooms/{room_number}'.format(hotel_id=56, room_number='room_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rooms_get_rooms(client):
    """Test case for rooms_get_rooms

    Get a list of rooms using the provided filtering and pagination criteria.
    """
    params = [('occupancy', 'occupancy_example'),
                    ('conditions', ['conditions_example']),
                    ('maintenances', ['maintenances_example']),
                    ('roomTypes', ['room_types_example']),
                    ('amenities', ['amenities_example']),
                    ('views', ['views_example']),
                    ('locations', ['locations_example']),
                    ('skip', 56),
                    ('top', 56),
                    ('inlinecount', 'inlinecount_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/rooms'.format(hotel_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rooms_get_rooms_count(client):
    """Test case for rooms_get_rooms_count

    Get the count of all rooms in the hotel matching the given filter criteria.
    """
    params = [('occupancy', 'occupancy_example'),
                    ('conditions', ['conditions_example']),
                    ('maintenances', ['maintenances_example']),
                    ('roomTypes', ['room_types_example']),
                    ('amenities', ['amenities_example']),
                    ('views', ['views_example']),
                    ('locations', ['locations_example'])]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/rooms/$count'.format(hotel_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_rooms_patch_room(client):
    """Test case for rooms_patch_room

    Partially updates a room.
    """
    patch_request = [openapi_server.OperationRoomPatchRequest()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api/hotel/v0/hotels/{hotel_id}/rooms/{room_number}'.format(hotel_id=56, room_number='room_number_example'),
        headers=headers,
        json=patch_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

