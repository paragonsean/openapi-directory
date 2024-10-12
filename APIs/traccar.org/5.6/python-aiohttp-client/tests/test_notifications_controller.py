# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification import Notification
from openapi_server.models.notification_type import NotificationType


pytestmark = pytest.mark.asyncio

async def test_notifications_get(client):
    """Test case for notifications_get

    Fetch a list of Notifications
    """
    params = [('all', True),
                    ('userId', 56),
                    ('deviceId', 56),
                    ('groupId', 56),
                    ('refresh', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_id_delete(client):
    """Test case for notifications_id_delete

    Delete a Notification
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/notifications/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_id_put(client):
    """Test case for notifications_id_put

    Update a Notification
    """
    body = {"always":True,"calendarId":0,"mail":True,"web":True,"sms":True,"attributes":"{}","id":6,"type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/notifications/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_post(client):
    """Test case for notifications_post

    Create a Notification
    """
    body = {"always":True,"calendarId":0,"mail":True,"web":True,"sms":True,"attributes":"{}","id":6,"type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/notifications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_test_post(client):
    """Test case for notifications_test_post

    Send test notification to current user via Email and SMS
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/notifications/test',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_types_get(client):
    """Test case for notifications_types_get

    Fetch a list of available Notification types
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/notifications/types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

