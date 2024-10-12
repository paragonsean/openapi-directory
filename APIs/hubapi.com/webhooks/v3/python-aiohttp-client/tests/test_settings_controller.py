# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.settings_change_request import SettingsChangeRequest
from openapi_server.models.settings_response import SettingsResponse


pytestmark = pytest.mark.asyncio

async def test_delete_webhooks_v3_app_id_settings_clear(client):
    """Test case for delete_webhooks_v3_app_id_settings_clear

    
    """
    headers = { 
        'Accept': '*/*',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/webhooks/v3/{app_id}/settings'.format(app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhooks_v3_app_id_settings_get_all(client):
    """Test case for get_webhooks_v3_app_id_settings_get_all

    
    """
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/webhooks/v3/{app_id}/settings'.format(app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_webhooks_v3_app_id_settings_configure(client):
    """Test case for put_webhooks_v3_app_id_settings_configure

    
    """
    body = {"targetUrl":"https://www.example.com/hubspot/target","throttling":{"maxConcurrentRequests":10,"period":"SECONDLY"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/webhooks/v3/{app_id}/settings'.format(app_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

