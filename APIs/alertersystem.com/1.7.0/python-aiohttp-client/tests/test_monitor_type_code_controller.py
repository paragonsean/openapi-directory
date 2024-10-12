# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_monitor_type_code_get_collection200_response import ApiMonitorTypeCodeGetCollection200Response
from openapi_server.models.monitor_type_code_get import MonitorTypeCodeGet
from openapi_server.models.monitor_type_code_jsonld_get import MonitorTypeCodeJsonldGet


pytestmark = pytest.mark.asyncio

async def test_api_monitor_type_code_get_collection(client):
    """Test case for api_monitor_type_code_get_collection

    Retrieves the collection of MonitorTypeCode resources.
    """
    params = [('page', 1),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/monitor-type-code',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_monitor_type_code_id_get(client):
    """Test case for api_monitor_type_code_id_get

    Retrieves a MonitorTypeCode resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/monitor-type-code/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

