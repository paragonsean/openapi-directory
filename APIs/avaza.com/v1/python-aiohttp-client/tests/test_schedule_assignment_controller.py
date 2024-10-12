# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.schedule_assignment_list import ScheduleAssignmentList


pytestmark = pytest.mark.asyncio

async def test_schedule_assignment_get(client):
    """Test case for schedule_assignment_get

    Gets list of Schedule Assignments.
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('ScheduleDateFrom', '2013-10-20T19:20:30+01:00'),
                    ('ScheduleDateTo', '2013-10-20T19:20:30+01:00'),
                    ('ScheduleSeriesID', 56),
                    ('UserID', 56),
                    ('UserEmail', 'user_email_example'),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('Sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ScheduleAssignment',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

