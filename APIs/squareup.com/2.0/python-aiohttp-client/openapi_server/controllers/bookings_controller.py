from typing import List, Dict
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
from openapi_server import util


async def cancel_booking(request: web.Request, booking_id, body) -> web.Response:
    """CancelBooking

    Cancels an existing booking.

    :param booking_id: The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-cancelled booking.
    :type booking_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CancelBookingRequest.from_dict(body)
    return web.Response(status=200)


async def create_booking(request: web.Request, body) -> web.Response:
    """CreateBooking

    Creates a booking.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateBookingRequest.from_dict(body)
    return web.Response(status=200)


async def list_team_member_booking_profiles(request: web.Request, bookable_only=None, limit=None, cursor=None, location_id=None) -> web.Response:
    """ListTeamMemberBookingProfiles

    Lists booking profiles for team members.

    :param bookable_only: Indicates whether to include only bookable team members in the returned result (&#x60;true&#x60;) or not (&#x60;false&#x60;).
    :type bookable_only: bool
    :param limit: The maximum number of results to return.
    :type limit: int
    :param cursor: The cursor for paginating through the results.
    :type cursor: str
    :param location_id: Indicates whether to include only team members enabled at the given location in the returned result.
    :type location_id: str

    """
    return web.Response(status=200)


async def retrieve_booking(request: web.Request, booking_id) -> web.Response:
    """RetrieveBooking

    Retrieves a booking.

    :param booking_id: The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-retrieved booking.
    :type booking_id: str

    """
    return web.Response(status=200)


async def retrieve_business_booking_profile(request: web.Request, ) -> web.Response:
    """RetrieveBusinessBookingProfile

    Retrieves a seller&#39;s booking profile.


    """
    return web.Response(status=200)


async def retrieve_team_member_booking_profile(request: web.Request, team_member_id) -> web.Response:
    """RetrieveTeamMemberBookingProfile

    Retrieves a team member&#39;s booking profile.

    :param team_member_id: The ID of the team member to retrieve.
    :type team_member_id: str

    """
    return web.Response(status=200)


async def search_availability(request: web.Request, body) -> web.Response:
    """SearchAvailability

    Searches for availabilities for booking.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchAvailabilityRequest.from_dict(body)
    return web.Response(status=200)


async def update_booking(request: web.Request, booking_id, body) -> web.Response:
    """UpdateBooking

    Updates a booking.

    :param booking_id: The ID of the [Booking](https://developer.squareup.com/reference/square_2021-08-18/objects/Booking) object representing the to-be-updated booking.
    :type booking_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateBookingRequest.from_dict(body)
    return web.Response(status=200)
