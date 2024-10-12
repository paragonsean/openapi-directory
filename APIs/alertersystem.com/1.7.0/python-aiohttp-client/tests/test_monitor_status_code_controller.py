# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_monitor_status_code_get_collection200_response import ApiMonitorStatusCodeGetCollection200Response
from openapi_server.models.monitor_status_code_get import MonitorStatusCodeGet
from openapi_server.models.monitor_status_code_jsonld_get import MonitorStatusCodeJsonldGet


pytestmark = pytest.mark.asyncio

async def test_api_monitor_status_code_get_collection(client):
    """Test case for api_monitor_status_code_get_collection

    Retrieves the collection of MonitorStatusCode resources.
    """
    params = [('page', 1),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/monitor-status-code',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_monitor_status_code_id_get(client):
    """Test case for api_monitor_status_code_id_get

    Retrieves a MonitorStatusCode resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/monitor-status-code/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

