# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.spending_pulse_list_response import SpendingPulseListResponse


pytestmark = pytest.mark.asyncio

async def test_spendingpulse_get(client):
    """Test case for spendingpulse_get

    Returns all Spending Pulse reports (with the exception of the gasoline weekly report, which has its own resource), that one is subscribed to.
    """
    params = [('CurrentRow', '1'),
                    ('Offset', '25'),
                    ('ProductLine', 'Weekly Sales'),
                    ('PublicationCoveragePeriod', 'March 2015'),
                    ('Country', 'US'),
                    ('ReportType', 'reportA'),
                    ('Period', 'Weekly'),
                    ('Sector', 'sectorA'),
                    ('Ecomm', 'Y')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/spendingpulse/v1/spulse.svc/spendingpulse',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

