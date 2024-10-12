# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.diary_appointment_details import DiaryAppointmentDetails
from openapi_server.models.diary_appointment_model import DiaryAppointmentModel
from openapi_server.models.diary_appointment_model_results import DiaryAppointmentModelResults
from openapi_server.models.diary_appointment_type_model_results import DiaryAppointmentTypeModelResults
from openapi_server.models.diary_booking_model import DiaryBookingModel
from openapi_server.models.feedback_submission_model import FeedbackSubmissionModel
from openapi_server.models.guest_diary_parameters_results_model import GuestDiaryParametersResultsModel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_diary_controller_add_feedback(client):
    """Test case for diary_controller_add_feedback

    Submit appointment feedback
    """
    body = {"Feedback":"Feedback","AppointmentID":"AppointmentID","PropertyID":"PropertyID"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/diary/{short_name}/appointment/feedback'.format(short_name='short_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diary_controller_cancel_appointment(client):
    """Test case for diary_controller_cancel_appointment

    Cancel an existing appointment using its unique identifier
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/diary/{short_name}/appointment/{appointment_id}/cancel'.format(short_name='short_name_example', appointment_id='appointment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diary_controller_delete_appointment(client):
    """Test case for diary_controller_delete_appointment

    Delete an existing appointment using its unique identifier
    """
    params = [('appointmentID', 'appointment_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/diary/{short_name}/appointment'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diary_controller_get_allocations(client):
    """Test case for diary_controller_get_allocations

    Get a list of all available allocations for a date + 7 days for a specified appointment type
    """
    params = [('preferredDate', '2013-10-20T19:20:30+01:00'),
                    ('appointmentType', 'appointment_type_example'),
                    ('lettings', True),
                    ('propertyIdentifier', 'property_identifier_example'),
                    ('branchID', 'branch_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/diary/{short_name}/allocations'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diary_controller_get_appointment(client):
    """Test case for diary_controller_get_appointment

    Get an appointment by ID
    """
    params = [('appointmentID', 'appointment_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/diary/{short_name}/appointment'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diary_controller_get_appointment_types(client):
    """Test case for diary_controller_get_appointment_types

    A collection of all diary appointment types
    """
    params = [('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/diary/{short_name}/appointmenttypes'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diary_controller_get_appointments_between_dates(client):
    """Test case for diary_controller_get_appointments_between_dates

    A collection of diary appointments linked to a company filtered between specific dates and by appointment type
    """
    params = [('branchID', 'branch_id_example'),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('appointmentTypesToSearch', ['appointment_types_to_search_example']),
                    ('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/diary/{short_name}/appointmentsbetweendates'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diary_controller_get_recurring_appointments(client):
    """Test case for diary_controller_get_recurring_appointments

    Retrieves all recurring appointments:-
    """
    params = [('branchID', 'branch_id_example'),
                    ('appointmentTypesToSearch', ['appointment_types_to_search_example']),
                    ('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/diary/{short_name}/recurringappointment'.format(short_name='short_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_diary_controller_post_appointment(client):
    """Test case for diary_controller_post_appointment

    Post an appointment into a valid diary allocation
    """
    body = {"AllocationDetails":{"StaffID":"StaffID","Start":"2000-01-23T04:56:07.000+00:00","End":"2000-01-23T04:56:07.000+00:00","StaffName":"StaffName"},"AppointmentType":"AppointmentType","Guests":[{"Forename":"Forename","AllowMarketingCorrespondence":True,"OID":"OID","Surname":"Surname","EmailAddress":"EmailAddress","MobilePhone":"MobilePhone"},{"Forename":"Forename","AllowMarketingCorrespondence":True,"OID":"OID","Surname":"Surname","EmailAddress":"EmailAddress","MobilePhone":"MobilePhone"}],"Subject":"Subject","ExtraComments":"ExtraComments"}
    params = [('propertyIdentifier', ['property_identifier_example']),
                    ('lettings', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/diary/{short_name}/appointment'.format(short_name='short_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_diary_controller_put_appointment(client):
    """Test case for diary_controller_put_appointment

    Update an existing appointment using its unique identifier
    """
    body = {"AllocationDetails":{"StaffID":"StaffID","Start":"2000-01-23T04:56:07.000+00:00","End":"2000-01-23T04:56:07.000+00:00","StaffName":"StaffName"},"AppointmentType":"AppointmentType","Guests":[{"Forename":"Forename","AllowMarketingCorrespondence":True,"OID":"OID","Surname":"Surname","EmailAddress":"EmailAddress","MobilePhone":"MobilePhone"},{"Forename":"Forename","AllowMarketingCorrespondence":True,"OID":"OID","Surname":"Surname","EmailAddress":"EmailAddress","MobilePhone":"MobilePhone"}],"Subject":"Subject","ExtraComments":"ExtraComments"}
    params = [('appointmentID', 'appointment_id_example'),
                    ('lettings', True),
                    ('AllowMarketingCorrespondence', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v3/diary/{short_name}/appointment'.format(short_name='short_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diary_controller_search_guest(client):
    """Test case for diary_controller_search_guest

    Match Guest Parameters with existing applicants
    """
    params = [('forename', 'forename_example'),
                    ('emailaddress', 'emailaddress_example'),
                    ('surname', 'surname_example'),
                    ('offset', 56),
                    ('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/diary/{shortname}/{branch_id}/guest/search'.format(shortname='shortname_example', branch_id='branch_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

