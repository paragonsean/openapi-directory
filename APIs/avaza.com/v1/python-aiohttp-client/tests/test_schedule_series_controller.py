# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_booking import CreateBooking
from openapi_server.models.create_leave import CreateLeave
from openapi_server.models.edit_booking import EditBooking
from openapi_server.models.edit_leave import EditLeave
from openapi_server.models.schedule_series_details import ScheduleSeriesDetails
from openapi_server.models.schedule_series_list import ScheduleSeriesList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_schedule_series_add_booking(client):
    """Test case for schedule_series_add_booking

    Create new Schedule Booking
    """
    model = {"DurationType":"DurationType","StartDate":"2000-01-23T04:56:07.000+00:00","CategoryIDFK":0,"HoursPerDay":6.027456183070403,"ProjectIDFK":1,"TaskIDFK":5,"UserIDFK":2,"EndDate":"2000-01-23T04:56:07.000+00:00","ScheduleOnDaysOff":True,"Notes":"Notes","TotalDuration":5.637376656633329}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ScheduleSeries/AddBooking',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_schedule_series_add_leave(client):
    """Test case for schedule_series_add_leave

    Create new Leave Booking
    """
    model = {"LeaveUserIDFK":1,"LeaveEndDate":"2000-01-23T04:56:07.000+00:00","LeaveTypeIDFK":6,"LeaveStartDate":"2000-01-23T04:56:07.000+00:00","LeaveHoursPerDay":0.8008281904610115,"LeaveNotify":True,"LeaveNotes":"LeaveNotes"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/ScheduleSeries/AddLeave',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_schedule_series_edit_booking(client):
    """Test case for schedule_series_edit_booking

    Edit Booking
    """
    model = {"DurationType":"DurationType","StartDate":"2000-01-23T04:56:07.000+00:00","CategoryIDFK":0,"HoursPerDay":6.027456183070403,"ScheduleSeriesID":5,"ProjectIDFK":1,"TaskIDFK":5,"UserIDFK":7,"EndDate":"2000-01-23T04:56:07.000+00:00","ScheduleOnDaysOff":True,"Notes":"Notes","TotalDuration":2.3021358869347655}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/ScheduleSeries/EditBooking',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_schedule_series_edit_leave(client):
    """Test case for schedule_series_edit_leave

    Edit Leave Booking
    """
    model = {"StartDate":"2000-01-23T04:56:07.000+00:00","LeaveTypeIDFK":6,"HoursPerDay":0.8008281904610115,"ScheduleSeriesID":1,"UserIDFK":5,"EndDate":"2000-01-23T04:56:07.000+00:00","Notes":"Notes"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/ScheduleSeries/EditLeave',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedule_series_get(client):
    """Test case for schedule_series_get

    Gets list of Schedule Series
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('ScheduleStartDateFrom', '2013-10-20T19:20:30+01:00'),
                    ('ScheduleStartDateTo', '2013-10-20T19:20:30+01:00'),
                    ('ScheduleEndDateFrom', '2013-10-20T19:20:30+01:00'),
                    ('ScheduleEndDateTo', '2013-10-20T19:20:30+01:00'),
                    ('UserID', 56),
                    ('UserEmail', 'user_email_example'),
                    ('TimeSheetCategoryID', 56),
                    ('TimeSheetCategoryName', 'time_sheet_category_name_example'),
                    ('LeaveTypeID', 56),
                    ('ProjectID', 56),
                    ('CompanyID', 56),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('Sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ScheduleSeries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

