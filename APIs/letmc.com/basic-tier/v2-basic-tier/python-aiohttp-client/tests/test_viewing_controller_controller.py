# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.viewing_booking_model import ViewingBookingModel


pytestmark = pytest.mark.asyncio

async def test_viewing_controller_get_bookings(client):
    """Test case for viewing_controller_get_bookings

    Gets a list of available viewing slots for one or more properties
    """
    params = [('preferredDate', '2013-10-20T19:20:30+01:00'),
                    ('propertyIDsToView', ['property_ids_to_view_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/tier2/{short_name}/viewing/bookings'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_viewing_controller_make_booking(client):
    """Test case for viewing_controller_make_booking

    Book an appointment for a viewing slot returned from the GET verb
    """
    selected_viewing_slot = {"StaffID":"StaffID","Start":"2000-01-23T04:56:07.000+00:00","End":"2000-01-23T04:56:07.000+00:00","StaffName":"StaffName"}
    params = [('forename', 'forename_example'),
                    ('surname', 'surname_example'),
                    ('mobilePhone', 'mobile_phone_example'),
                    ('emailAddress', 'email_address_example'),
                    ('propertyIDsToView', ['property_ids_to_view_example']),
                    ('wantRoomInSharedProperty', True),
                    ('alertMinRent', 3.4),
                    ('alertMaxRent', 3.4),
                    ('alertNumberOfBeds', 56),
                    ('alertAreaID', 'alert_area_id_example'),
                    ('alertTenantType', 'alert_tenant_type_example'),
                    ('subscribeToEmailAlerts', True),
                    ('subscribeToSMSAlerts', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/tier2/{short_name}/viewing/bookings'.format(short_name='short_name_example'),
        headers=headers,
        json=selected_viewing_slot,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

