# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.availability_input_model import AvailabilityInputModel
from openapi_server.models.resource_block_view_model import ResourceBlockViewModel
from openapi_server.models.resource_list_view_model import ResourceListViewModel
from openapi_server.models.service_allocation_input_model import ServiceAllocationInputModel
from openapi_server.models.service_allocation_list_view_model import ServiceAllocationListViewModel
from openapi_server.models.service_allocation_update_model import ServiceAllocationUpdateModel
from openapi_server.models.service_allocation_view_model import ServiceAllocationViewModel
from openapi_server.models.service_allocations_input_model import ServiceAllocationsInputModel
from openapi_server.models.service_availability_view_model import ServiceAvailabilityViewModel
from openapi_server.models.service_block_input_model import ServiceBlockInputModel
from openapi_server.models.service_block_list_view_model import ServiceBlockListViewModel
from openapi_server.models.service_block_update_model import ServiceBlockUpdateModel
from openapi_server.models.service_block_view_model import ServiceBlockViewModel
from openapi_server.models.service_calendar_input_model import ServiceCalendarInputModel
from openapi_server.models.service_calendar_view_model import ServiceCalendarViewModel
from openapi_server.models.service_image_input_model import ServiceImageInputModel
from openapi_server.models.service_input_model import ServiceInputModel
from openapi_server.models.service_list_view_model import ServiceListViewModel
from openapi_server.models.service_update_model import ServiceUpdateModel
from openapi_server.models.service_view_model import ServiceViewModel


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_allocations_id_delete(client):
    """Test case for setup_v1_services_allocations_id_delete

    Delete Allocation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/services/allocations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_allocations_id_get(client):
    """Test case for setup_v1_services_allocations_id_get

    Get Allocation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/services/allocations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_services_allocations_id_put(client):
    """Test case for setup_v1_services_allocations_id_put

    Update Allocation
    """
    body = {"reason":"reason","repeats":True,"resourceId":"resourceId","endDate":"2000-01-23","locationId":"locationId","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":1,"bookingLimit":0,"endTime":6,"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/services/allocations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_block_id_delete(client):
    """Test case for setup_v1_services_block_id_delete

    Delete Block
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/services/block/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_services_block_id_put(client):
    """Test case for setup_v1_services_block_id_put

    Update Block
    """
    body = {"reason":"reason","repeats":True,"endDate":"2000-01-23","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":5,"endTime":0,"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/services/block/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_blocks_id_get(client):
    """Test case for setup_v1_services_blocks_id_get

    Get Block
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/services/blocks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_calendar_id_delete(client):
    """Test case for setup_v1_services_calendar_id_delete

    Delete Service Links
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/services/calendar/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_services_calendar_post(client):
    """Test case for setup_v1_services_calendar_post

    Link Service to Calendar
    """
    body = {"calendarId":"calendarId","locationId":"locationId","serviceId":"serviceId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/services/calendar',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_get(client):
    """Test case for setup_v1_services_get

    List Services
    """
    params = [('locationId', 'location_id_example'),
                    ('serviceGroupId', 56),
                    ('deleted', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_services_id_allocations_bulk_post(client):
    """Test case for setup_v1_services_id_allocations_bulk_post

    Create Allocations Bulk
    """
    body = {"serviceAllocations":[{"reason":"reason","repeats":True,"resourceId":"resourceId","endDate":"2000-01-23","locationId":"locationId","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":1,"bookingLimit":0,"endTime":6,"startDate":"2000-01-23"},{"reason":"reason","repeats":True,"resourceId":"resourceId","endDate":"2000-01-23","locationId":"locationId","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":1,"bookingLimit":0,"endTime":6,"startDate":"2000-01-23"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/services/{id}/allocations/bulk'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_id_allocations_get(client):
    """Test case for setup_v1_services_id_allocations_get

    List Service Allocations
    """
    params = [('locationId', 'location_id_example'),
                    ('resourceId', 'resource_id_example'),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/services/{id}/allocations'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_services_id_allocations_post(client):
    """Test case for setup_v1_services_id_allocations_post

    Create Allocation
    """
    body = {"reason":"reason","repeats":True,"resourceId":"resourceId","endDate":"2000-01-23","locationId":"locationId","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":1,"bookingLimit":0,"endTime":6,"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/services/{id}/allocations'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_id_availability_get(client):
    """Test case for setup_v1_services_id_availability_get

    Get Weekly Availability
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/services/{id}/availability'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_services_id_availability_put(client):
    """Test case for setup_v1_services_id_availability_put

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
        path='/setup/v1/services/{id}/availability'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_services_id_block_post(client):
    """Test case for setup_v1_services_id_block_post

    Create Block
    """
    body = {"reason":"reason","repeats":True,"endDate":"2000-01-23","locationId":"locationId","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":6,"endTime":0,"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/services/{id}/block'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_id_blocks_get(client):
    """Test case for setup_v1_services_id_blocks_get

    List Service Blocks
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
        path='/setup/v1/services/{id}/blocks'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_id_calendar_get(client):
    """Test case for setup_v1_services_id_calendar_get

    Get Linked Calendar
    """
    params = [('locationId', 'location_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/services/{id}/calendar'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_id_delete(client):
    """Test case for setup_v1_services_id_delete

    Delete Service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/services/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_id_deleteimage_delete(client):
    """Test case for setup_v1_services_id_deleteimage_delete

    Delete Service Image
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/services/{id}/deleteimage'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_id_get(client):
    """Test case for setup_v1_services_id_get

    Get Service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/services/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_services_id_put(client):
    """Test case for setup_v1_services_id_put

    Update Service
    """
    body = {"settings":{"bookAheadValue":1,"bookInAdvance":1,"bookAheadUnit":7},"fees":{"feeAmount":5.637376656633329,"cancellationFeeAmount":5.962133916683182,"feeTaxable":True,"nonRefundable":True,"cancellationFeeTaxable":True},"customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"bookingInterval":0,"description":"description","maxCapacity":2,"availability":{"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}},"bookingLimit":6,"type":"type","duration":1,"public":True,"locationId":"locationId","mediaPageUrl":"mediaPageUrl","name":"name","options":{"durationMax":3,"padding":4,"consumerPadding":True,"durationSelect":True,"durationInterval":9,"defaultService":True,"durationMin":2},"maxGroupSize":7,"serviceGroupId":"serviceGroupId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/services/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_id_recover_put(client):
    """Test case for setup_v1_services_id_recover_put

    Recover Service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/services/{id}/recover'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_services_id_resources_get(client):
    """Test case for setup_v1_services_id_resources_get

    List Resources for Service
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('googleAuthReturnUrl', 'google_auth_return_url_example'),
                    ('outlookAuthReturnUrl', 'outlook_auth_return_url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/services/{id}/resources'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_services_id_uploadimage_post(client):
    """Test case for setup_v1_services_id_uploadimage_post

    Upload Service Image
    """
    body = {"imageFileData":"imageFileData","imageFileName":"imageFileName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/services/{id}/uploadimage'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_services_post(client):
    """Test case for setup_v1_services_post

    Create Service
    """
    body = {"settings":{"bookAheadValue":1,"bookInAdvance":1,"bookAheadUnit":7},"fees":{"feeAmount":5.637376656633329,"cancellationFeeAmount":5.962133916683182,"feeTaxable":True,"nonRefundable":True,"cancellationFeeTaxable":True},"customFields":{"field1":"field1","field10":"field10","field7":"field7","field6":"field6","field9":"field9","field8":"field8","field3":"field3","field2":"field2","field5":"field5","field4":"field4"},"bookingInterval":0,"description":"description","maxCapacity":2,"availability":{"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}},"bookingLimit":6,"type":"type","duration":1,"public":True,"locationId":"locationId","mediaPageUrl":"mediaPageUrl","name":"name","options":{"durationMax":3,"padding":4,"consumerPadding":True,"durationSelect":True,"durationInterval":9,"defaultService":True,"durationMin":2},"maxGroupSize":7,"serviceGroupId":"serviceGroupId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/services',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

