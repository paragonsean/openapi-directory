# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.notification import Notification
from openapi_server.models.notification_error import NotificationError
from openapi_server.models.notification_list_update_data import NotificationListUpdateData
from openapi_server.models.notification_settings import NotificationSettings
from openapi_server.models.notification_settings_data import NotificationSettingsData
from openapi_server.models.notification_settings_error import NotificationSettingsError
from openapi_server.models.notification_update_data import NotificationUpdateData


pytestmark = pytest.mark.asyncio

async def test_notification_read(client):
    """Test case for notification_read

    Retrieve a specific notification.
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/notifications/{notification_id}'.format(namespace='namespace_example', notification_id='notification_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_settings_create(client):
    """Test case for notification_settings_create

    Create global notification settings
    """
    notification_settings_data = {"emails_enabled":True,"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/notifications/settings'.format(namespace='namespace_example'),
        headers=headers,
        json=notification_settings_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_settings_entity_create(client):
    """Test case for notification_settings_entity_create

    Create global notification settings
    """
    notification_settings_data = {"emails_enabled":True,"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{namespace}/notifications/settings/entity/{entity}'.format(namespace='namespace_example', entity='entity_example'),
        headers=headers,
        json=notification_settings_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_settings_entity_read(client):
    """Test case for notification_settings_entity_read

    Retrieve global notification settings for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/notifications/settings/entity/{entity}'.format(namespace='namespace_example', entity='entity_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_settings_entity_update(client):
    """Test case for notification_settings_entity_update

    Modify global notification settings.
    """
    notification_settings_data = {"emails_enabled":True,"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/notifications/settings/entity/{entity}'.format(namespace='namespace_example', entity='entity_example'),
        headers=headers,
        json=notification_settings_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_settings_read(client):
    """Test case for notification_settings_read

    Retrieve global notification settings for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/notifications/settings'.format(namespace='namespace_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_settings_update(client):
    """Test case for notification_settings_update

    Modify global notification settings.
    """
    notification_settings_data = {"emails_enabled":True,"enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/notifications/settings'.format(namespace='namespace_example'),
        headers=headers,
        json=notification_settings_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_update(client):
    """Test case for notification_update

    Mark a specific notification as either read or unread.
    """
    notification_data = {"read":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/notifications/{notification_id}'.format(namespace='namespace_example', notification_id='notification_id_example'),
        headers=headers,
        json=notification_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_list(client):
    """Test case for notifications_list

    Get notifications of all types and entities for the authenticated user.
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example'),
                    ('read', True)]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/notifications'.format(namespace='namespace_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_list_entity(client):
    """Test case for notifications_list_entity

    Get notifications of all types and entities for the authenticated user.
    """
    params = [('limit', 'limit_example'),
                    ('offset', 'offset_example'),
                    ('ordering', 'ordering_example'),
                    ('read', True)]
    headers = { 
        'Accept': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{namespace}/notifications/entity/{entity}'.format(namespace='namespace_example', entity='entity_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_update_entity_list(client):
    """Test case for notifications_update_entity_list

    Mark a list of notifications as either read or unread.
    """
    notification_data = {"read":True,"notifications":["notifications","notifications"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/notifications/entity/{entity}'.format(namespace='namespace_example', entity='entity_example'),
        headers=headers,
        json=notification_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_update_list(client):
    """Test case for notifications_update_list

    Mark a list of notifications as either read or unread.
    """
    notification_data = {"read":True,"notifications":["notifications","notifications"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'jwt': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/{namespace}/notifications'.format(namespace='namespace_example'),
        headers=headers,
        json=notification_data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

