# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.report import Report
from openapi_server.models.report_request import ReportRequest
from openapi_server.models.report_response import ReportResponse


pytestmark = pytest.mark.asyncio

async def test_reports_create(client):
    """Test case for reports_create

    Create a new report.
    """
    body = {"process":"process","file_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-v1/reports/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_list(client):
    """Test case for reports_list

    Get user report list.
    """
    headers = { 
        'Accept': 'application/json',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-v1/reports/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reports_read(client):
    """Test case for reports_read

    Get report details.
    """
    headers = { 
        'Accept': 'application/json',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-v1/reports/{report_number}'.format(report_number='report_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

