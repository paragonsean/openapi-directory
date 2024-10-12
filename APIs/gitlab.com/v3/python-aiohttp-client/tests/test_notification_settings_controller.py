# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.global_notification_setting import GlobalNotificationSetting
from openapi_server.models.put_v3_notification_settings_request import PutV3NotificationSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_v3_notification_settings(client):
    """Test case for get_v3_notification_settings

    Get global notification level settings and email, defaults to Participate
    """
    headers = { 
        'Accept': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/notification_settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_v3_notification_settings(client):
    """Test case for put_v3_notification_settings

    Update global notification level settings and email, defaults to Participate
    """
    body = openapi_server.PutV3NotificationSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'private_token_query': 'special-key',
        'private_token_header': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/notification_settings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

