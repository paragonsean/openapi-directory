# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_log_status_code_get import AlertLogStatusCodeGet
from openapi_server.models.alert_log_status_code_jsonld_get import AlertLogStatusCodeJsonldGet
from openapi_server.models.api_alert_log_status_code_get_collection200_response import ApiAlertLogStatusCodeGetCollection200Response


pytestmark = pytest.mark.asyncio

async def test_api_alert_log_status_code_get_collection(client):
    """Test case for api_alert_log_status_code_get_collection

    Retrieves the collection of AlertLogStatusCode resources.
    """
    params = [('page', 1),
                    ('properties[]', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alert-log-status-code',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_alert_log_status_code_id_get(client):
    """Test case for api_alert_log_status_code_id_get

    Retrieves a AlertLogStatusCode resource.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/alert-log-status-code/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

