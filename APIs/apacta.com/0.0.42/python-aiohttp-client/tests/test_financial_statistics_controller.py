# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.financial_statistics_working_hours_get200_response import FinancialStatisticsWorkingHoursGet200Response


pytestmark = pytest.mark.asyncio

async def test_financial_statistics_working_hours_get(client):
    """Test case for financial_statistics_working_hours_get

    Get Total working hours grouped by time entry type
    """
    params = [('date_from', '2013-10-20'),
                    ('date_to', '2013-10-20'),
                    ('project_id', 'project_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/financial_statistics/workingHours',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

