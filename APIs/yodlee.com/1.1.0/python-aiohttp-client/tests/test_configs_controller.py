# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.configs_notification_response import ConfigsNotificationResponse
from openapi_server.models.configs_public_key_response import ConfigsPublicKeyResponse
from openapi_server.models.create_configs_notification_event_request import CreateConfigsNotificationEventRequest
from openapi_server.models.update_configs_notification_event_request import UpdateConfigsNotificationEventRequest
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_create_subscription_notification_event(client):
    """Test case for create_subscription_notification_event

    Subscribe For Notification Event
    """
    body = {"event":{"callbackUrl":"callbackUrl"}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/configs/notifications/events/{event_name}'.format(event_name='event_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_subscribed_notification_event(client):
    """Test case for delete_subscribed_notification_event

    Delete Notification Subscription
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/configs/notifications/events/{event_name}'.format(event_name='event_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_encryption_key(client):
    """Test case for get_public_encryption_key

    Get Public Key
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/configs/publicKey',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscribed_notification_events(client):
    """Test case for get_subscribed_notification_events

    Get Subscribed Notification Events
    """
    params = [('eventName', 'event_name_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/configs/notifications/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_subscribed_notification_event(client):
    """Test case for update_subscribed_notification_event

    Update Notification Subscription
    """
    body = {"event":{"callbackUrl":"callbackUrl"}}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/configs/notifications/events/{event_name}'.format(event_name='event_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

