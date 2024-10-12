# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_monitor_status_log_get_collection200_response import ApiMonitorStatusLogGetCollection200Response
from openapi_server.models.monitor_status_log_get import MonitorStatusLogGet
from openapi_server.models.monitor_status_log_jsonld_get import MonitorStatusLogJsonldGet


pytestmark = pytest.mark.asyncio

async def test_api_monitor_status_log_get_collection(client):
    """Test case for api_monitor_status_log_get_collection

    Retrieves the collection of MonitorStatusLog resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('monitor', 'monitor_example'),
                    ('monitor[]', ['monitor_example']),
                    ('monitorStatusCode', 'monitor_status_code_example'),
                    ('monitorStatusCode[]', ['monitor_status_code_example']),
                    ('partition', 'partition_example'),
                    ('partition[]', ['partition_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/monitor-status-log',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_monitor_status_log_id_get(client):
    """Test case for api_monitor_status_log_id_get

    Retrieves a MonitorStatusLog resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/monitor-status-log/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

