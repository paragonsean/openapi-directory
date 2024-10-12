# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_booking_request import CancelBookingRequest
from openapi_server.models.cancel_booking_response import CancelBookingResponse
from openapi_server.models.create_booking_request import CreateBookingRequest
from openapi_server.models.create_booking_response import CreateBookingResponse
from openapi_server.models.list_team_member_booking_profiles_response import ListTeamMemberBookingProfilesResponse
from openapi_server.models.retrieve_booking_response import RetrieveBookingResponse
from openapi_server.models.retrieve_business_booking_profile_response import RetrieveBusinessBookingProfileResponse
from openapi_server.models.retrieve_team_member_booking_profile_response import RetrieveTeamMemberBookingProfileResponse
from openapi_server.models.search_availability_request import SearchAvailabilityRequest
from openapi_server.models.search_availability_response import SearchAvailabilityResponse
from openapi_server.models.update_booking_request import UpdateBookingRequest
from openapi_server.models.update_booking_response import UpdateBookingResponse


pytestmark = pytest.mark.asyncio

async def test_cancel_booking(client):
    """Test case for cancel_booking

    CancelBooking
    """
    body = {"booking_version":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/bookings/{booking_id}/cancel'.format(booking_id='booking_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_booking(client):
    """Test case for create_booking

    CreateBooking
    """
    body = {"booking":{"appointment_segments":[{"duration_minutes":60,"service_variation_id":"RU3PBTZTK7DXZDQFCJHOK2MC","service_variation_version":1599775456731,"team_member_id":"TMXUrsBWWcHTt79t"}],"customer_id":"EX2QSVGTZN4K1E5QE1CBFNVQ8M","location_id":"LEQHH0YY8B42M","start_at":"2020-11-26T13:00:00Z"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/bookings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_team_member_booking_profiles(client):
    """Test case for list_team_member_booking_profiles

    ListTeamMemberBookingProfiles
    """
    params = [('bookable_only', True),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('location_id', 'location_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/bookings/team-member-booking-profiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_booking(client):
    """Test case for retrieve_booking

    RetrieveBooking
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/bookings/{booking_id}'.format(booking_id='booking_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_business_booking_profile(client):
    """Test case for retrieve_business_booking_profile

    RetrieveBusinessBookingProfile
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/bookings/business-booking-profile',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_team_member_booking_profile(client):
    """Test case for retrieve_team_member_booking_profile

    RetrieveTeamMemberBookingProfile
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/bookings/team-member-booking-profiles/{team_member_id}'.format(team_member_id='team_member_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_availability(client):
    """Test case for search_availability

    SearchAvailability
    """
    body = {"query":{"filter":{"location_id":"LEQHH0YY8B42M","segment_filters":[{"service_variation_id":"RU3PBTZTK7DXZDQFCJHOK2MC","team_member_id_filter":{"any":["TMXUrsBWWcHTt79t","TMaJcbiRqPIGZuS9"]}}],"start_at_range":{"end_at":"2020-11-27T13:00:00Z","start_at":"2020-11-26T13:00:00Z"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/bookings/availability/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_booking(client):
    """Test case for update_booking

    UpdateBooking
    """
    body = {"booking":{"customer_note":"I would like to sit near the window please","version":1}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/bookings/{booking_id}'.format(booking_id='booking_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

