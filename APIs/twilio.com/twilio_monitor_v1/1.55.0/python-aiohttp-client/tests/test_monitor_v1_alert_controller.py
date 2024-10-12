# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_alert_response import ListAlertResponse
from openapi_server.models.monitor_v1_alert_instance import MonitorV1AlertInstance


pytestmark = pytest.mark.asyncio

async def test_fetch_alert(client):
    """Test case for fetch_alert

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Alerts/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_alert(client):
    """Test case for list_alert

    
    """
    params = [('LogLevel', 'log_level_example'),
                    ('StartDate', '2013-10-20T19:20:30+01:00'),
                    ('EndDate', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Alerts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

