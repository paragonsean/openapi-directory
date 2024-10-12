# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_timesheet import NewTimesheet
from openapi_server.models.timesheet_details import TimesheetDetails
from openapi_server.models.timesheet_list import TimesheetList
from openapi_server.models.update_timesheet_model import UpdateTimesheetModel


pytestmark = pytest.mark.asyncio

async def test_timesheet_delete(client):
    """Test case for timesheet_delete

    Delete a Timesheet Entry
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/Timesheet/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timesheet_get(client):
    """Test case for timesheet_get

    Gets list of Timsheets
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('EntryDateFrom', '2013-10-20T19:20:30+01:00'),
                    ('EntryDateTo', '2013-10-20T19:20:30+01:00'),
                    ('UserID', 56),
                    ('UserEmail', 'user_email_example'),
                    ('CategoryName', 'category_name_example'),
                    ('ProjectID', 56),
                    ('isBillable', True),
                    ('isInvoiced', True),
                    ('isTimerRunning', True),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('includeInvoiceDetails', True),
                    ('Sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Timesheet',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timesheet_get_by_id(client):
    """Test case for timesheet_get_by_id

    Gets a Timesheet Entry by Timesheet ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Timesheet/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_timesheet_post(client):
    """Test case for timesheet_post

    Create a new Timesheet Entry
    """
    model = {"hasStartEndTime":True,"ProjectIDFK":6,"TaskIDFK":1,"EntryDate":"2000-01-23T04:56:07.000+00:00","isInvoiced":True,"UserIDFK":5,"Duration":0.8008281904610115,"TimesheetCategoryIDFK":5,"Notes":"Notes","CustomMetadata":"CustomMetadata"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Timesheet',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_timesheet_put(client):
    """Test case for timesheet_put

    Update a Timesheet
    """
    model = {"TimeSheetEntryID":5,"FieldsToUpdate":["FieldsToUpdate","FieldsToUpdate"],"hasStartEndTime":True,"ProjectIDFK":6,"TaskIDFK":1,"EntryDate":"2000-01-23T04:56:07.000+00:00","Duration":0.8008281904610115,"TimesheetCategoryIDFK":5,"Notes":"Notes","CustomMetadata":"CustomMetadata"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/Timesheet',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

