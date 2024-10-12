# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.daily_quality_response import DailyQualityResponse
from openapi_server.models.overall_quality_response import OverallQualityResponse


pytestmark = pytest.mark.asyncio

async def test_quality_get_daily_data_quality_for_site(client):
    """Test case for quality_get_daily_data_quality_for_site

    Get Site DailyQuality
    """
    params = [('siteId', 'site_id_example'),
                    ('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v{version}/quality/daily'.format(version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_quality_get_overall_data_quality_for_sites(client):
    """Test case for quality_get_overall_data_quality_for_sites

    Get Site OverallQuality
    """
    params = [('sites', 'sites_example'),
                    ('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v{version}/quality/overall'.format(version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

