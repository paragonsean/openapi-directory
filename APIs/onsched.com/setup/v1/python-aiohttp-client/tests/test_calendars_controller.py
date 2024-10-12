# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calendar_block_input_model import CalendarBlockInputModel
from openapi_server.models.calendar_block_list_view_model import CalendarBlockListViewModel
from openapi_server.models.calendar_block_update_model import CalendarBlockUpdateModel
from openapi_server.models.calendar_block_view_model import CalendarBlockViewModel
from openapi_server.models.resource_block_view_model import ResourceBlockViewModel
from openapi_server.models.schedule_input_model import ScheduleInputModel
from openapi_server.models.schedule_list_view_model import ScheduleListViewModel
from openapi_server.models.schedule_update_model import ScheduleUpdateModel
from openapi_server.models.schedule_view_model import ScheduleViewModel
from openapi_server.models.service_list_view_model import ServiceListViewModel


pytestmark = pytest.mark.asyncio

async def test_setup_v1_calendars_block_id_delete(client):
    """Test case for setup_v1_calendars_block_id_delete

    Delete Calendar Block
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/calendars/block/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_calendars_block_id_put(client):
    """Test case for setup_v1_calendars_block_id_put

    Update Calendar Block
    """
    body = {"reason":"reason","repeats":True,"endDate":"2000-01-23","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":5,"endTime":0,"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/calendars/block/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_calendars_blocks_id_get(client):
    """Test case for setup_v1_calendars_blocks_id_get

    Get Calendar Block
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/calendars/blocks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_calendars_get(client):
    """Test case for setup_v1_calendars_get

    List Calendars
    """
    params = [('locationId', 'location_id_example'),
                    ('deleted', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/calendars',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_calendars_id_block_post(client):
    """Test case for setup_v1_calendars_id_block_post

    Create Calendar Block
    """
    body = {"reason":"reason","repeats":True,"endDate":"2000-01-23","repeat":{"weekdays":"weekdays","monthDay":1,"interval":6,"monthType":"monthType","frequency":"frequency"},"startTime":6,"endTime":0,"startDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/calendars/{id}/block'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_calendars_id_blocks_get(client):
    """Test case for setup_v1_calendars_id_blocks_get

    List Calendar Blocks
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/calendars/{id}/blocks'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_calendars_id_delete(client):
    """Test case for setup_v1_calendars_id_delete

    Delete Calendar
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/calendars/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_calendars_id_get(client):
    """Test case for setup_v1_calendars_id_get

    Get Calendar
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/calendars/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_calendars_id_put(client):
    """Test case for setup_v1_calendars_id_put

    Update Calendar
    """
    body = {"locationId":"locationId","name":"name","interval":6,"resourceGroupId":"resourceGroupId","availability":{"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}},"type":"type","bookingsPerSlot":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/calendars/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_calendars_id_recover_put(client):
    """Test case for setup_v1_calendars_id_recover_put

    Recover Calendar
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/calendars/{id}/recover'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_calendars_id_services_get(client):
    """Test case for setup_v1_calendars_id_services_get

    List Calendar Services
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/calendars/{id}/services'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_calendars_post(client):
    """Test case for setup_v1_calendars_post

    DEPRECATING: Create
    """
    body = {"locationId":"locationId","name":"name","interval":5,"resourceGroupId":"resourceGroupId","availability":{"thu":{"startTime":6,"endTime":0},"tue":{"startTime":6,"endTime":0},"sat":{"startTime":6,"endTime":0},"wed":{"startTime":6,"endTime":0},"fri":{"startTime":6,"endTime":0},"mon":{"startTime":6,"endTime":0},"sun":{"startTime":6,"endTime":0}},"type":"type","bookingsPerSlot":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/calendars',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

