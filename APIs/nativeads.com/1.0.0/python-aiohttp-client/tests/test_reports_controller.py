# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.model_error import ModelError
from openapi_server.models.reports_daily_response import ReportsDailyResponse
from openapi_server.models.reports_website_response import ReportsWebsiteResponse
from openapi_server.models.reports_widget_response import ReportsWidgetResponse


pytestmark = pytest.mark.asyncio

async def test_publisher_reports_daily_get(client):
    """Test case for publisher_reports_daily_get

    
    """
    params = [('token', 'token_example'),
                    ('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20'),
                    ('limit', 100),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/publisher/reports/daily',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publisher_reports_website_get(client):
    """Test case for publisher_reports_website_get

    
    """
    params = [('token', 'token_example'),
                    ('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20'),
                    ('limit', 100),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/publisher/reports/website',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publisher_reports_widget_get(client):
    """Test case for publisher_reports_widget_get

    
    """
    params = [('token', 'token_example'),
                    ('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20'),
                    ('limit', 100),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/publisher/reports/widget',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

