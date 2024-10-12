# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_log_get import AlertLogGet
from openapi_server.models.alert_log_jsonld_get import AlertLogJsonldGet
from openapi_server.models.api_alert_log_get_collection200_response import ApiAlertLogGetCollection200Response


pytestmark = pytest.mark.asyncio

async def test_api_alert_log_get_collection(client):
    """Test case for api_alert_log_get_collection

    Retrieves the collection of AlertLog resources.
    """
    params = [('page', 1),
                    ('dataSegmentCode', 'data_segment_code_example'),
                    ('dataSegmentCode[]', ['data_segment_code_example']),
                    ('monitor', 'monitor_example'),
                    ('monitor[]', ['monitor_example']),
                    ('alertService', 'alert_service_example'),
                    ('alertService[]', ['alert_service_example']),
                    ('alertLogStatusCode', 'alert_log_status_code_example'),
                    ('alertLogStatusCode[]', ['alert_log_status_code_example']),
                    ('partition', 'partition_example'),
                    ('partition[]', ['partition_example']),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alert-log',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_alert_log_id_get(client):
    """Test case for api_alert_log_id_get

    Retrieves a AlertLog resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alert-log/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

