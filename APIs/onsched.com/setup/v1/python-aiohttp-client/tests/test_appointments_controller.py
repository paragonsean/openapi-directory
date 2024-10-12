# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.appointment_list_view_model import AppointmentListViewModel
from openapi_server.models.appointment_view_model import AppointmentViewModel


pytestmark = pytest.mark.asyncio

async def test_setup_v1_appointments_get(client):
    """Test case for setup_v1_appointments_get

    List Appointments
    """
    params = [('locationId', 'location_id_example'),
                    ('email', 'email_example'),
                    ('lastname', 'lastname_example'),
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
        path='/setup/v1/appointments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_appointments_id_get(client):
    """Test case for setup_v1_appointments_id_get

    Get Appointment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/appointments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_appointments_id_reassign_resource_resource_id_put(client):
    """Test case for setup_v1_appointments_id_reassign_resource_resource_id_put

    Reassign Appointment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/appointments/{id}/reassign/resource/{resource_id}'.format(id='id_example', resource_id='resource_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

