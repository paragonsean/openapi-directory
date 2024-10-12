# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assign_room_criteria import AssignRoomCriteria
from openapi_server.models.assign_room_response import AssignRoomResponse
from openapi_server.models.authorization_request import AuthorizationRequest
from openapi_server.models.base_response import BaseResponse
from openapi_server.models.booking_list_response import BookingListResponse
from openapi_server.models.cancellation_response import CancellationResponse
from openapi_server.models.check_in_details import CheckInDetails
from openapi_server.models.operation_reservation_patchable_model import OperationReservationPatchableModel
from openapi_server.models.reservation import Reservation
from openapi_server.models.reservation_confirmation import ReservationConfirmation
from openapi_server.models.reservation_response import ReservationResponse
from openapi_server.models.reservations_response import ReservationsResponse
from openapi_server.models.terminal_authorization_request import TerminalAuthorizationRequest
from openapi_server.models.total_count_response import TotalCountResponse


pytestmark = pytest.mark.asyncio

async def test_bookings_cancel_reservation(client):
    """Test case for bookings_cancel_reservation

    Cancel one reservation.
    """
    params = [('sendConfirmation', True)]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/booking/v0/bookings/{confirmation_id}/reservations/{reservation_number}/cancel'.format(confirmation_id='confirmation_id_example', reservation_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bookings_check_in(client):
    """Test case for bookings_check_in

    Performs a check in operation for a reservation.
    """
    check_in_details = {"client_identity":"client_identity"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/booking/v0/bookings/{confirmation_id}/reservations/{reservation_number}/check_in'.format(confirmation_id='confirmation_id_example', reservation_number=56),
        headers=headers,
        json=check_in_details,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bookings_check_out(client):
    """Test case for bookings_check_out

    Performs a check out operation for a reservation.
    """
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/booking/v0/bookings/{confirmation_id}/reservations/{reservation_number}/check_out'.format(confirmation_id='confirmation_id_example', reservation_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bookings_create_booking(client):
    """Test case for bookings_create_booking

    Create a new booking.
    """
    reservation = {"rooms":5,"prepay_discount":5.962133916683182,"group_code":"group_code","addons":["addons","addons"],"adults":0,"departure_date":"2000-01-23T04:56:07.000+00:00","hotel_id":1,"guarantee":{"guarantee_type":"PM4Hold","token":{"authorization_reference":"authorization_reference","token_id":"token_id","authorization_expiry_date":"2000-01-23T04:56:07.000+00:00","merchant_reference":"merchant_reference","authorized_amount":6.027456183070403,"shopper_email":"shopper_email","shopper_reference":"shopper_reference","authorization_status":"Authorized"}},"external_id":"external_id","channel_code":"channel_code","rate_plan":"rate_plan","travel_agent":{"company_id":"company_id"},"contact":{"customer_id":"customer_id"},"guests":[{"mailing_address":{"country":"country","address":"address","address_type":"Home","city":"city","postal_code":"postal_code"},"consent_subscribe":["consent_subscribe","consent_subscribe"],"gender":"Unspecified","nationality":"nationality","phone":"phone","consent_unsubscribe":["consent_unsubscribe","consent_unsubscribe"],"last_name":"last_name","customer_id":"customer_id","title":"title","first_name":"first_name","email":"email","primary":True},{"mailing_address":{"country":"country","address":"address","address_type":"Home","city":"city","postal_code":"postal_code"},"consent_subscribe":["consent_subscribe","consent_subscribe"],"gender":"Unspecified","nationality":"nationality","phone":"phone","consent_unsubscribe":["consent_unsubscribe","consent_unsubscribe"],"last_name":"last_name","customer_id":"customer_id","title":"title","first_name":"first_name","email":"email","primary":True}],"comment":"comment","company":{"company_id":"company_id"},"arrival_date":"2000-01-23T04:56:07.000+00:00","payment_method":"None","room_type":"room_type"}
    params = [('sendConfirmation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/booking/v0/bookings',
        headers=headers,
        json=reservation,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bookings_get_booking(client):
    """Test case for bookings_get_booking

    Load all reservations for one booking by confirmation id.
    """
    params = [('expand', 'expand_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/booking/v0/bookings/{confirmation_id}'.format(confirmation_id='confirmation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bookings_get_bookings(client):
    """Test case for bookings_get_bookings

    Find bookings matching the given filter criteria.
    """
    params = [('hotelId', 56),
                    ('cancellationId', 'cancellation_id_example'),
                    ('reservationNumber', 56),
                    ('customerName', 'customer_name_example'),
                    ('customerEmail', 'customer_email_example'),
                    ('customerId', 'customer_id_example'),
                    ('roomNumber', 'room_number_example'),
                    ('externalId', 'external_id_example'),
                    ('companyName', 'company_name_example'),
                    ('companyId', 'company_id_example'),
                    ('companyEmail', 'company_email_example'),
                    ('blockCode', 'block_code_example'),
                    ('reservationStatuses', ['reservation_statuses_example']),
                    ('marketCodes', ['market_codes_example']),
                    ('channelCodes', ['channel_codes_example']),
                    ('subChannelCodes', ['sub_channel_codes_example']),
                    ('roomTypes', ['room_types_example']),
                    ('ratePlanCodes', ['rate_plan_codes_example']),
                    ('labels', ['labels_example']),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('dateFilter', 'date_filter_example'),
                    ('exclude', 'exclude_example'),
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
        path='/api/booking/v0/bookings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bookings_get_bookings_count(client):
    """Test case for bookings_get_bookings_count

    Get total count of bookings matchung the given filter criteria.
    """
    params = [('hotelId', 56),
                    ('cancellationId', 'cancellation_id_example'),
                    ('reservationNumber', 56),
                    ('customerName', 'customer_name_example'),
                    ('customerEmail', 'customer_email_example'),
                    ('customerId', 'customer_id_example'),
                    ('roomNumber', 'room_number_example'),
                    ('externalId', 'external_id_example'),
                    ('companyName', 'company_name_example'),
                    ('companyId', 'company_id_example'),
                    ('companyEmail', 'company_email_example'),
                    ('blockCode', 'block_code_example'),
                    ('reservationStatuses', ['reservation_statuses_example']),
                    ('marketCodes', ['market_codes_example']),
                    ('channelCodes', ['channel_codes_example']),
                    ('subChannelCodes', ['sub_channel_codes_example']),
                    ('roomTypes', ['room_types_example']),
                    ('ratePlanCodes', ['rate_plan_codes_example']),
                    ('labels', ['labels_example']),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('dateFilter', 'date_filter_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/booking/v0/bookings/$count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bookings_get_reservation(client):
    """Test case for bookings_get_reservation

    Load a specific reservation from a booking.
    """
    params = [('expand', 'expand_example'),
                    ('exclude', 'exclude_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/booking/v0/bookings/{confirmation_id}/reservations/{reservation_number}'.format(confirmation_id='confirmation_id_example', reservation_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bookings_patch(client):
    """Test case for bookings_patch

    Partially updates a reservation.
    """
    patch_request = [openapi_server.OperationReservationPatchableModel()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api/booking/v0/bookings/{confirmation_id}/reservations/{reservation_number}'.format(confirmation_id='confirmation_id_example', reservation_number=56),
        headers=headers,
        json=patch_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bookings_payment_token(client):
    """Test case for bookings_payment_token

    Post a payment token for a reservation.
    """
    authorization_request = {"authorization":{"reference":"reference","amount":0.8008281904610115,"merchant_reference":"merchant_reference","expiry_date":"2000-01-23T04:56:07.000+00:00","shopper_reference":"shopper_reference"},"no_authorization_required":True,"payment_token":"payment_token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/booking/v0/bookings/{confirmation_id}/reservations/{reservation_number}/payment_token'.format(confirmation_id='confirmation_id_example', reservation_number=56),
        headers=headers,
        json=authorization_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bookings_post_room_assignment(client):
    """Test case for bookings_post_room_assignment

    Assign a room to a reservation.
    """
    assigning_criteria = {"amenities":["amenities","amenities"],"condition":"CleanNotInspected","respect_guest_preferences":True,"include_out_of_service":True,"room_number":"room_number","locations":["locations","locations"],"views":["views","views"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/booking/v0/bookings/{confirmation_id}/reservations/{reservation_number}/assign_room'.format(confirmation_id='confirmation_id_example', reservation_number=56),
        headers=headers,
        json=assigning_criteria,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bookings_terminal_authorization(client):
    """Test case for bookings_terminal_authorization

    Performs a chip and pin credit card authorization for a reservation.
    """
    authorization_request = {"client_identity":"client_identity","amount_to_authorize":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api/booking/v0/bookings/{confirmation_id}/reservations/{reservation_number}/pre_authorize'.format(confirmation_id='confirmation_id_example', reservation_number=56),
        headers=headers,
        json=authorization_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

