# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.appointment_view_model import AppointmentViewModel
from openapi_server.models.availability_input_model import AvailabilityInputModel
from openapi_server.models.calendar_auth_view_model import CalendarAuthViewModel
from openapi_server.models.resource_allocation_input_model import ResourceAllocationInputModel
from openapi_server.models.resource_allocation_list_view_model import ResourceAllocationListViewModel
from openapi_server.models.resource_allocation_update_model import ResourceAllocationUpdateModel
from openapi_server.models.resource_allocation_view_model import ResourceAllocationViewModel
from openapi_server.models.resource_availability_view_model import ResourceAvailabilityViewModel
from openapi_server.models.resource_block_input_model import ResourceBlockInputModel
from openapi_server.models.resource_block_list_view_model import ResourceBlockListViewModel
from openapi_server.models.resource_block_update_model import ResourceBlockUpdateModel
from openapi_server.models.resource_block_view_model import ResourceBlockViewModel
from openapi_server.models.resource_image_input_model import ResourceImageInputModel
from openapi_server.models.resource_input_model import ResourceInputModel
from openapi_server.models.resource_list_view_model import ResourceListViewModel
from openapi_server.models.resource_update_model import ResourceUpdateModel
from openapi_server.models.resource_view_model import ResourceViewModel
from openapi_server.models.resources_input_model import ResourcesInputModel
from openapi_server.models.resources_update_model import ResourcesUpdateModel
from openapi_server.models.system_timezone_view_model import SystemTimezoneViewModel


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_allocations_id_delete(client):
    """Test case for setup_v1_resources_allocations_id_delete

    Delete Allocation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/resources/allocations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_allocations_id_get(client):
    """Test case for setup_v1_resources_allocations_id_get

    Get Allocation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resources/allocations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_allocations_id_put(client):
    """Test case for setup_v1_resources_allocations_id_put

    Update Allocation
    """
    body = {"reason":"reason","repeats":True,"endDate":"2000-01-23","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":6,"endTime":0,"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/resources/allocations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_block_id_delete(client):
    """Test case for setup_v1_resources_block_id_delete

    Delete Block
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/resources/block/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_block_id_put(client):
    """Test case for setup_v1_resources_block_id_put

    Update Block
    """
    body = {"allDay":True,"reason":"reason","repeats":True,"endDate":"2000-01-23","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":6,"endTime":0,"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/resources/block/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_blocks_id_get(client):
    """Test case for setup_v1_resources_blocks_id_get

    Get Block
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resources/blocks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_bulk_post(client):
    """Test case for setup_v1_resources_bulk_post

    Create Resources Bulk
    """
    body = {"resources":[{"address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"recurringAvailability":True,"groupId":"groupId","description":"description","availability":{"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}},"serviceIds":["serviceIds","serviceIds"],"locationId":"locationId","contact":{"mobilePhone":"mobilePhone","businessPhoneExt":"businessPhoneExt","skypeUsername":"skypeUsername","homePhone":"homePhone","conferenceInfo":"conferenceInfo","preferredPhoneType":"preferredPhoneType","businessPhone":"businessPhone"},"name":"name","options":{"ignoreBusinessHours":True,"googleCalendarId":"googleCalendarId","sortKey":7,"gender":"gender","bookingNotification":9,"hourly":2.027123023002322,"displayColor":"displayColor","notificationType":4,"calendarAvailability":3,"bioLink":"bioLink","outlookCalendarId":"outlookCalendarId","effectiveDate":"2000-01-23T04:56:07.000+00:00"},"timezoneId":"timezoneId","email":"email"},{"address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"recurringAvailability":True,"groupId":"groupId","description":"description","availability":{"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}},"serviceIds":["serviceIds","serviceIds"],"locationId":"locationId","contact":{"mobilePhone":"mobilePhone","businessPhoneExt":"businessPhoneExt","skypeUsername":"skypeUsername","homePhone":"homePhone","conferenceInfo":"conferenceInfo","preferredPhoneType":"preferredPhoneType","businessPhone":"businessPhone"},"name":"name","options":{"ignoreBusinessHours":True,"googleCalendarId":"googleCalendarId","sortKey":7,"gender":"gender","bookingNotification":9,"hourly":2.027123023002322,"displayColor":"displayColor","notificationType":4,"calendarAvailability":3,"bioLink":"bioLink","outlookCalendarId":"outlookCalendarId","effectiveDate":"2000-01-23T04:56:07.000+00:00"},"timezoneId":"timezoneId","email":"email"}]}
    params = [('googleAuthReturnUrl', 'google_auth_return_url_example'),
                    ('outlookAuthReturnUrl', 'outlook_auth_return_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/resources/bulk',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_bulk_put(client):
    """Test case for setup_v1_resources_bulk_put

    Update Resources Bulk
    """
    body = {"resources":[{"address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"recurringAvailability":True,"groupId":"groupId","description":"description","availability":{"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}},"serviceIds":["serviceIds","serviceIds"],"contact":{"mobilePhone":"mobilePhone","businessPhoneExt":"businessPhoneExt","skypeUsername":"skypeUsername","homePhone":"homePhone","conferenceInfo":"conferenceInfo","preferredPhoneType":"preferredPhoneType","businessPhone":"businessPhone"},"name":"name","options":{"ignoreBusinessHours":True,"googleCalendarId":"googleCalendarId","sortKey":5,"gender":"gender","bookingNotification":0,"hourly":1.4658129805029452,"displayColor":"displayColor","notificationType":5,"calendarAvailability":6,"bioLink":"bioLink","outlookCalendarId":"outlookCalendarId","effectiveDate":"2000-01-23T04:56:07.000+00:00"},"timezoneId":"timezoneId","id":"id","email":"email"},{"address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"recurringAvailability":True,"groupId":"groupId","description":"description","availability":{"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}},"serviceIds":["serviceIds","serviceIds"],"contact":{"mobilePhone":"mobilePhone","businessPhoneExt":"businessPhoneExt","skypeUsername":"skypeUsername","homePhone":"homePhone","conferenceInfo":"conferenceInfo","preferredPhoneType":"preferredPhoneType","businessPhone":"businessPhone"},"name":"name","options":{"ignoreBusinessHours":True,"googleCalendarId":"googleCalendarId","sortKey":5,"gender":"gender","bookingNotification":0,"hourly":1.4658129805029452,"displayColor":"displayColor","notificationType":5,"calendarAvailability":6,"bioLink":"bioLink","outlookCalendarId":"outlookCalendarId","effectiveDate":"2000-01-23T04:56:07.000+00:00"},"timezoneId":"timezoneId","id":"id","email":"email"}]}
    params = [('googleAuthReturnUrl', 'google_auth_return_url_example'),
                    ('outlookAuthReturnUrl', 'outlook_auth_return_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/resources/bulk',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_get(client):
    """Test case for setup_v1_resources_get

    List Resources
    """
    params = [('locationId', 'location_id_example'),
                    ('resourceGroupId', 'resource_group_id_example'),
                    ('email', 'email_example'),
                    ('name', 'name_example'),
                    ('deleted', True),
                    ('googleAuthReturnUrl', 'google_auth_return_url_example'),
                    ('outlookAuthReturnUrl', 'outlook_auth_return_url_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resources',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_allocations_get(client):
    """Test case for setup_v1_resources_id_allocations_get

    List Resource Allocations
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resources/{id}/allocations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_id_allocations_post(client):
    """Test case for setup_v1_resources_id_allocations_post

    Create Allocation
    """
    body = {"reason":"reason","repeats":True,"endDate":"2000-01-23","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":6,"endTime":0,"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/resources/{id}/allocations'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_availability_get(client):
    """Test case for setup_v1_resources_id_availability_get

    List Weekly Availability
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resources/{id}/availability'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_id_availability_put(client):
    """Test case for setup_v1_resources_id_availability_put

    Update Weekly Availability
    """
    body = {"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/resources/{id}/availability'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_id_block_post(client):
    """Test case for setup_v1_resources_id_block_post

    Create Block
    """
    body = {"allDay":True,"reason":"reason","repeats":True,"endDate":"2000-01-23","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":6,"endTime":0,"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/resources/{id}/block'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_blocks_get(client):
    """Test case for setup_v1_resources_id_blocks_get

    List Resource Blocks
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resources/{id}/blocks'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_calendar_auth_google_google_email_address_get(client):
    """Test case for setup_v1_resources_id_calendar_auth_google_google_email_address_get

    Get Resource Google URL
    """
    params = [('googleAuthReturnUrl', 'google_auth_return_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resources/{id}/calendar/auth/google/{google_email_address}'.format(id='id_example', google_email_address='google_email_address_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_calendar_auth_outlook_outlook_email_address_get(client):
    """Test case for setup_v1_resources_id_calendar_auth_outlook_outlook_email_address_get

    Get Resource Outlook URL
    """
    params = [('outlookAuthReturnUrl', 'outlook_auth_return_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resources/{id}/calendar/auth/outlook/{outlook_email_address}'.format(id='id_example', outlook_email_address='outlook_email_address_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_delete(client):
    """Test case for setup_v1_resources_id_delete

    Delete Resource
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/resources/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_deleteimage_delete(client):
    """Test case for setup_v1_resources_id_deleteimage_delete

    Delete Resource Image
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/resources/{id}/deleteimage'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_get(client):
    """Test case for setup_v1_resources_id_get

    Get Resource
    """
    params = [('googleAuthReturnUrl', 'google_auth_return_url_example'),
                    ('outlookAuthReturnUrl', 'outlook_auth_return_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resources/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_id_put(client):
    """Test case for setup_v1_resources_id_put

    Update Resource
    """
    body = {"address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"recurringAvailability":True,"groupId":"groupId","description":"description","availability":{"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}},"serviceIds":["serviceIds","serviceIds"],"locationId":"locationId","contact":{"mobilePhone":"mobilePhone","businessPhoneExt":"businessPhoneExt","skypeUsername":"skypeUsername","homePhone":"homePhone","conferenceInfo":"conferenceInfo","preferredPhoneType":"preferredPhoneType","businessPhone":"businessPhone"},"name":"name","options":{"ignoreBusinessHours":True,"googleCalendarId":"googleCalendarId","sortKey":5,"gender":"gender","bookingNotification":0,"hourly":1.4658129805029452,"displayColor":"displayColor","notificationType":5,"calendarAvailability":6,"bioLink":"bioLink","outlookCalendarId":"outlookCalendarId","effectiveDate":"2000-01-23T04:56:07.000+00:00"},"timezoneId":"timezoneId","email":"email"}
    params = [('googleAuthReturnUrl', 'google_auth_return_url_example'),
                    ('outlookAuthReturnUrl', 'outlook_auth_return_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/resources/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_reassign_appointments_resource_id_put(client):
    """Test case for setup_v1_resources_id_reassign_appointments_resource_id_put

    Reassign Resource
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('calendarId', 'calendar_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/resources/{id}/reassign/appointments/{resource_id}'.format(id='id_example', resource_id='resource_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_recover_put(client):
    """Test case for setup_v1_resources_id_recover_put

    Recover Resource
    """
    params = [('googleAuthReturnUrl', 'google_auth_return_url_example'),
                    ('outlookAuthReturnUrl', 'outlook_auth_return_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/resources/{id}/recover'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_id_services_delete(client):
    """Test case for setup_v1_resources_id_services_delete

    Delete Linked Services
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/resources/{id}/services'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_id_services_post(client):
    """Test case for setup_v1_resources_id_services_post

    Create Linked Services
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/resources/{id}/services'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_id_services_put(client):
    """Test case for setup_v1_resources_id_services_put

    Update Linked Services
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/resources/{id}/services'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_id_uploadimage_post(client):
    """Test case for setup_v1_resources_id_uploadimage_post

    Upload Resource Image
    """
    body = {"imageFileData":"imageFileData","imageFileName":"imageFileName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/resources/{id}/uploadimage'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_resources_post(client):
    """Test case for setup_v1_resources_post

    Create Resource
    """
    body = {"address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"recurringAvailability":True,"groupId":"groupId","description":"description","availability":{"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}},"serviceIds":["serviceIds","serviceIds"],"locationId":"locationId","contact":{"mobilePhone":"mobilePhone","businessPhoneExt":"businessPhoneExt","skypeUsername":"skypeUsername","homePhone":"homePhone","conferenceInfo":"conferenceInfo","preferredPhoneType":"preferredPhoneType","businessPhone":"businessPhone"},"name":"name","options":{"ignoreBusinessHours":True,"googleCalendarId":"googleCalendarId","sortKey":7,"gender":"gender","bookingNotification":9,"hourly":2.027123023002322,"displayColor":"displayColor","notificationType":4,"calendarAvailability":3,"bioLink":"bioLink","outlookCalendarId":"outlookCalendarId","effectiveDate":"2000-01-23T04:56:07.000+00:00"},"timezoneId":"timezoneId","email":"email"}
    params = [('googleAuthReturnUrl', 'google_auth_return_url_example'),
                    ('outlookAuthReturnUrl', 'outlook_auth_return_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/resources',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_resources_timezones_get(client):
    """Test case for setup_v1_resources_timezones_get

    Get Time Zones
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/resources/timezones',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

