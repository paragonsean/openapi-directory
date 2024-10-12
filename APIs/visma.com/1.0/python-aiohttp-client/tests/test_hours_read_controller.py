# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billable_status_type import BillableStatusType
from openapi_server.models.deleted_work_hour_model import DeletedWorkHourModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.time_entry_model import TimeEntryModel
from openapi_server.models.work_hour_output_model import WorkHourOutputModel


pytestmark = pytest.mark.asyncio

async def test_time_entries_get_time_entries(client):
    """Test case for time_entries_get_time_entries

    Get the time entries.
    """
    params = [('firstRow', 0),
                    ('phaseGuid', ['phase_guid_example']),
                    ('timeEntryTypeGuid', ['time_entry_type_guid_example']),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/timeentries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entries_get_time_entries_for_user(client):
    """Test case for time_entries_get_time_entries_for_user

    Get all the time entries for a user.
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('phaseGuid', ['phase_guid_example']),
                    ('timeEntryTypeGuid', ['time_entry_type_guid_example']),
                    ('firstRow', 0),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/timeentries'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_time_entries_get_time_entry(client):
    """Test case for time_entries_get_time_entry

    Get time entry by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/timeentries/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hours_get_deleted_work_hours(client):
    """Test case for work_hours_get_deleted_work_hours

    Get the deleted work hours.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('projectGuids', ['project_guids_example']),
                    ('userGuids', ['user_guids_example']),
                    ('deletedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/deletedworkhours',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hours_get_project_work_hours(client):
    """Test case for work_hours_get_project_work_hours

    Get all the work hours for phases of a project for invoicing
    """
    params = [('isBillable', True),
                    ('isBilled', True),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/workhours'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hours_get_work_hour(client):
    """Test case for work_hours_get_work_hour

    Get work hour by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/workhours/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hours_get_work_hours(client):
    """Test case for work_hours_get_work_hours

    Get the work hours.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('billableStatus', openapi_server.BillableStatusType()),
                    ('eventDateStart', '2013-10-20'),
                    ('eventDateEnd', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/workhours',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hours_get_work_hours_for_user(client):
    """Test case for work_hours_get_work_hours_for_user

    Get all the work hours for a user
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('phaseGuid', ['phase_guid_example']),
                    ('workTypeGuid', ['work_type_guid_example']),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/workhours'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

