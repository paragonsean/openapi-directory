# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.appointment_book_model import AppointmentBookModel
from openapi_server.models.appointment_initial_model import AppointmentInitialModel
from openapi_server.models.appointment_initial_view_model import AppointmentInitialViewModel
from openapi_server.models.appointment_list_view_model import AppointmentListViewModel
from openapi_server.models.appointment_reschedule_model import AppointmentRescheduleModel
from openapi_server.models.appointment_reserve_model import AppointmentReserveModel
from openapi_server.models.appointment_view_model import AppointmentViewModel
from openapi_server.models.booking_field_list_view_model import BookingFieldListViewModel
from openapi_server.models.custom_field_definition_list_view_model import CustomFieldDefinitionListViewModel


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_appointments_bookingfields_get(client):
    """Test case for consumer_v1_appointments_bookingfields_get

    Get Custom Fields Labels
    """
    params = [('locationId', 'location_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/appointments/bookingfields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_appointments_customfields_get(client):
    """Test case for consumer_v1_appointments_customfields_get

    Get Custom Fields List
    """
    params = [('locationId', 'location_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/appointments/customfields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_appointments_get(client):
    """Test case for consumer_v1_appointments_get

    Get Appointments
    """
    params = [('locationId', 'location_id_example'),
                    ('email', 'email_example'),
                    ('lastname', 'lastname_example'),
                    ('phone', 'phone_example'),
                    ('serviceId', 'service_id_example'),
                    ('calendarId', 'calendar_id_example'),
                    ('resourceId', 'resource_id_example'),
                    ('customerId', 'customer_id_example'),
                    ('serviceAllocationId', 'service_allocation_id_example'),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('status', 'status_example'),
                    ('bookedBy', 'booked_by_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/appointments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_consumer_v1_appointments_id_book_put(client):
    """Test case for consumer_v1_appointments_id_book_put

    Book Appointment
    """
    body = {"phoneExt":"phoneExt","phoneType":"phoneType","customerMessage":"customerMessage","notes":"notes","phone":"phone","customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"customerBookingFields":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"name":"name","groupSize":0,"appointmentBookingFields":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/consumer/v1/appointments/{id}/book'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_appointments_id_cancel_put(client):
    """Test case for consumer_v1_appointments_id_cancel_put

    Cancel Appointment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/consumer/v1/appointments/{id}/cancel'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_appointments_id_confirm_put(client):
    """Test case for consumer_v1_appointments_id_confirm_put

    Confirm Appointment
    """
    params = [('undo', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/consumer/v1/appointments/{id}/confirm'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_appointments_id_delete(client):
    """Test case for consumer_v1_appointments_id_delete

    Delete Appointment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/consumer/v1/appointments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_v1_appointments_id_get(client):
    """Test case for consumer_v1_appointments_id_get

    Get Appointment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/consumer/v1/appointments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_consumer_v1_appointments_id_noshow_put(client):
    """Test case for consumer_v1_appointments_id_noshow_put

    Set NoShow Status
    """
    body = None
    headers = { 
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/consumer/v1/appointments/{id}/noshow'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_consumer_v1_appointments_id_reschedule_put(client):
    """Test case for consumer_v1_appointments_id_reschedule_put

    Reschedule Appointment
    """
    body = {"resourceId":"resourceId","travelAppointmentId":"travelAppointmentId","startDateTime":"2000-01-23T04:56:07.000+00:00","travelTimeMins":0,"endDateTime":"2000-01-23T04:56:07.000+00:00","serviceId":"serviceId","resourceIds":"resourceIds"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/consumer/v1/appointments/{id}/reschedule'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_consumer_v1_appointments_id_reserve_put(client):
    """Test case for consumer_v1_appointments_id_reserve_put

    Reserve Appointment
    """
    body = {"phoneExt":"phoneExt","phoneType":"phoneType","customerMessage":"customerMessage","notes":"notes","phone":"phone","customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"customerBookingFields":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"name":"name","appointmentBookingFields":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"email":"email"}
    params = [('sendNotifications', True)]
    headers = { 
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/consumer/v1/appointments/{id}/reserve'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_consumer_v1_appointments_post(client):
    """Test case for consumer_v1_appointments_post

    Create Appointment
    """
    body = {"resourceId":"resourceId","notes":"notes","customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"travelAppointmentId":"travelAppointmentId","customerBookingFields":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"locationId":"locationId","bookingWindowId":"bookingWindowId","customerId":"customerId","resourceGroupId":"resourceGroupId","serviceAllocationId":"serviceAllocationId","serviceId":"serviceId","email":"email","resourceIds":"resourceIds","phoneType":"phoneType","customerMessage":"customerMessage","travelTimeMins":6,"appointmentBookingFields":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"endDateTime":"2000-01-23T04:56:07.000+00:00","startDateTime":"2000-01-23T04:56:07.000+00:00","calendarId":"calendarId","phone":"phone","name":"name","timezoneName":"timezoneName","groupSize":0,"location":"location","bookedBy":"bookedBy"}
    params = [('completeBooking', 'complete_booking_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/consumer/v1/appointments',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

