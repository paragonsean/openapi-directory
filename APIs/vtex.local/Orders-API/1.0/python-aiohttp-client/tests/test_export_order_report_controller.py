# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.export_completed_response import ExportCompletedResponse
from openapi_server.models.export_in_progress_response import ExportInProgressResponse


pytestmark = pytest.mark.asyncio

async def test_status_completed(client):
    """Test case for status_completed

    Export order report with status 'Completed'
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oms/pvt/admin/reports/completed',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_status_in_progress(client):
    """Test case for status_in_progress

    Export order report with status 'In Progress'
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oms/pvt/admin/reports/inprogress',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

