# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_daily_report_all_countries200_response_inner import GetDailyReportAllCountries200ResponseInner
from openapi_server.models.get_latest_country_data_by_name200_response_inner import GetLatestCountryDataByName200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_daily_report_all_countries(client):
    """Test case for get_daily_report_all_countries

    getDailyReportAllCountries
    """
    params = [('date', '_date_example'),
                    ('date-format', YYYY-MM-DD),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/report/country/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_daily_report_by_country_code(client):
    """Test case for get_daily_report_by_country_code

    getDailyReportByCountryCode
    """
    params = [('code', 'code_example'),
                    ('date', '_date_example'),
                    ('date-format', YYYY-MM-DD),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/report/country/code',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_daily_report_by_country_name(client):
    """Test case for get_daily_report_by_country_name

    getDailyReportByCountryName
    """
    params = [('name', 'name_example'),
                    ('date', '_date_example'),
                    ('date-format', YYYY-MM-DD),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/report/country/name',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_all_countries(client):
    """Test case for get_latest_all_countries

    getLatestAllCountries
    """
    params = [('format', json)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/country/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_country_data_by_code(client):
    """Test case for get_latest_country_data_by_code

    getLatestCountryDataByCode
    """
    params = [('code', 'code_example'),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/country/code',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_country_data_by_name(client):
    """Test case for get_latest_country_data_by_name

    getLatestCountryDataByName
    """
    params = [('name', 'name_example'),
                    ('format', json)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/country',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

