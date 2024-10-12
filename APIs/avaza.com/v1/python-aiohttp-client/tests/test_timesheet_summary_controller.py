# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.timesheet_summary_result import TimesheetSummaryResult


pytestmark = pytest.mark.asyncio

async def test_timesheet_summary_get(client):
    """Test case for timesheet_summary_get

    Gets Basic Summary of Timesheet Statistics
    """
    params = [('model.groupBy', ['model_group_by_example']),
                    ('model.entryDateFrom', '2013-10-20T19:20:30+01:00'),
                    ('model.entryDateTo', '2013-10-20T19:20:30+01:00'),
                    ('model.userID', [56]),
                    ('model.projectID', 56),
                    ('model.isBillable', True),
                    ('model.isInvoiced', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/TimesheetSummary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

