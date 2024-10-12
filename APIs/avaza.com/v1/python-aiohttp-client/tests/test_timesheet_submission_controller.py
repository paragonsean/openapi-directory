# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_timesheet_submission_post(client):
    """Test case for timesheet_submission_post

    Submit Timesheets for Approval.
    """
    params = [('SendNotifications', True),
                    ('WholeWeekOf', '2013-10-20T19:20:30+01:00'),
                    ('WholeDayOf', '2013-10-20T19:20:30+01:00'),
                    ('UserID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/TimesheetSubmission',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

