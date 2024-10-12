# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_daily_report_totals200_response_inner import GetDailyReportTotals200ResponseInner
from openapi_server.models.get_latest_totals200_response_inner import GetLatestTotals200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_daily_report_totals(client):
    """Test case for get_daily_report_totals

    getDailyReportTotals
    """
    params = [('date', '_date_example'),
                    ('date-format', YYYY-MM-DD),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/report/totals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_totals(client):
    """Test case for get_latest_totals

    getLatestTotals
    """
    params = [('format', json)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/totals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

