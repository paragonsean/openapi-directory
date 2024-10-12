# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_reports_index(client):
    """Test case for reports_index

    Gets the daily report.
    """
    params = [('sites', 'sites_example'),
                    ('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('reportSubTypeId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v{version}/reports/{report_type}'.format(report_type='report_type_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vversion_reports_start_date_to_end_date_report_type_get(client):
    """Test case for vversion_reports_start_date_to_end_date_report_type_get

    Gets the daily report.
    """
    params = [('sites', 'sites_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('reportSubTypeId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v{version}/reports/{start_date}/to/{end_date}/{report_type}'.format(report_type='report_type_example', start_date='start_date_example', end_date='end_date_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

