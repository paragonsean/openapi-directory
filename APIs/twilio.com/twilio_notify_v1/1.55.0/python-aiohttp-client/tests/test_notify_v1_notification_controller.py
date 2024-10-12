# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_enum_priority import NotificationEnumPriority
from openapi_server.models.notify_v1_service_notification import NotifyV1ServiceNotification


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_notification(client):
    """Test case for create_notification

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'action': 'action_example',
        'alexa': None,
        'apn': None,
        'body': 'body_example',
        'data': None,
        'delivery_callback_url': 'delivery_callback_url_example',
        'facebook_messenger': None,
        'fcm': None,
        'gcm': None,
        'identity': ['identity_example'],
        'priority': openapi_server.NotificationEnumPriority(),
        'segment': ['segment_example'],
        'sms': None,
        'sound': 'sound_example',
        'tag': ['tag_example'],
        'title': 'title_example',
        'to_binding': ['to_binding_example'],
        'ttl': 56
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Notifications'.format(service_sid='service_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

