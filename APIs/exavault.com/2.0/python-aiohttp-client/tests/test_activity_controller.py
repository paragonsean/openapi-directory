# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.session_activity_response import SessionActivityResponse
from openapi_server.models.webhook_activity_response import WebhookActivityResponse


pytestmark = pytest.mark.asyncio

async def test_get_session_logs(client):
    """Test case for get_session_logs

    Get activity logs
    """
    params = [('startDate', '2019-10-18T06:48:40Z'),
                    ('endDate', '2019-10-18T06:48:40Z'),
                    ('ipAddress', '127.0.0.1'),
                    ('username', 'jdoe'),
                    ('path', '/folder*'),
                    ('type', 'EDIT_SHARE'),
                    ('offset', 100),
                    ('limit', 10),
                    ('sort', '-date')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/activity/session',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhook_logs(client):
    """Test case for get_webhook_logs

    Get webhook logs
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('endpointUrl', 'endpoint_url_example'),
                    ('event', 'resources.upload'),
                    ('statusCode', 200),
                    ('resourcePath', '/folder*'),
                    ('username', 'exampleuser'),
                    ('offset', 100),
                    ('limit', 10),
                    ('sort', '-date,event')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/activity/webhooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

