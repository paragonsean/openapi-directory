# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.error import Error
from openapi_server.models.report_output import ReportOutput
from openapi_server.models.reports_output import ReportsOutput


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_batch_upload(client):
    """Test case for batch_upload

    Batch Upload
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'api-key': 'special-key',
    }
    data = FormData()
    data.add_field('file', ['/path/to/file'])
    response = await client.request(
        method='POST',
        path='/v1/reports/{report_id}/upload'.format(report_id='report_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_report(client):
    """Test case for create_report

    Create Report
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
    }
    data = {
        'name': 'name_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/reports',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report(client):
    """Test case for get_report

    Get Report
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/reports/{report_id}'.format(report_id='report_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_reports(client):
    """Test case for list_reports

    List Reports
    """
    params = [('start_key', 'start_key_example'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/reports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

