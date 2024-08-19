# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_schema import ErrorSchema
from openapi_server.models.gas_weekly_list_response import GasWeeklyListResponse


pytestmark = pytest.mark.asyncio

async def test_gasweekly_get(client):
    """Test case for gasweekly_get

    Returns the weekly gasoline report. This resource pulls back the report with ProductLine = \"US Weekly Gasoline Demand Report\". Keep in mind that you must be subscribed to the gasoline weekly report to be able to receive data back from this resource.
    """
    params = [('CurrentRow', '1'),
                    ('Offset', '25')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/spendingpulse/v1/spulse.svc/gasweekly',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

