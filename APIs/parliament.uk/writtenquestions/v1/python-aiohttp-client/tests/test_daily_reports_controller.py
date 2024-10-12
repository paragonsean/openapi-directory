# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.daily_report_view_model_search_result import DailyReportViewModelSearchResult
from openapi_server.models.house_enum import HouseEnum
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_api_dailyreports_dailyreports_get(client):
    """Test case for api_dailyreports_dailyreports_get

    Returns a list of daily reports
    """
    params = [('dateFrom', '2013-10-20T19:20:30+01:00'),
                    ('dateTo', '2013-10-20T19:20:30+01:00'),
                    ('house', openapi_server.HouseEnum()),
                    ('skip', 56),
                    ('take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/dailyreports/dailyreports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

