# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notifications import Notifications
from openapi_server.models.notifications_unread import NotificationsUnread


pytestmark = pytest.mark.asyncio

async def test_add_notifications_all_read(client):
    """Test case for add_notifications_all_read

    addNotificationsAllRead()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/notifications/all/read',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_board_by_id_notification(client):
    """Test case for get_notifications_board_by_id_notification

    getNotificationsBoardByIdNotification()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/board'.format(id_notification='id_notification_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_board_by_id_notification_by_field(client):
    """Test case for get_notifications_board_by_id_notification_by_field

    getNotificationsBoardByIdNotificationByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/board/{_field}'.format(id_notification='id_notification_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_by_id_notification(client):
    """Test case for get_notifications_by_id_notification

    getNotificationsByIdNotification()
    """
    params = [('display', 'display_example'),
                    ('entities', 'entities_example'),
                    ('fields', 'all'),
                    ('memberCreator', 'member_creator_example'),
                    ('memberCreator_fields', 'avatarHash, fullName, initials and username'),
                    ('board', 'board_example'),
                    ('board_fields', 'name'),
                    ('list', 'list_example'),
                    ('card', 'card_example'),
                    ('card_fields', 'name'),
                    ('organization', 'organization_example'),
                    ('organization_fields', 'displayName'),
                    ('member', 'member_example'),
                    ('member_fields', 'avatarHash, fullName, initials and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}'.format(id_notification='id_notification_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_by_id_notification_by_field(client):
    """Test case for get_notifications_by_id_notification_by_field

    getNotificationsByIdNotificationByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/{_field}'.format(id_notification='id_notification_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_card_by_id_notification(client):
    """Test case for get_notifications_card_by_id_notification

    getNotificationsCardByIdNotification()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/card'.format(id_notification='id_notification_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_card_by_id_notification_by_field(client):
    """Test case for get_notifications_card_by_id_notification_by_field

    getNotificationsCardByIdNotificationByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/card/{_field}'.format(id_notification='id_notification_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_display_by_id_notification(client):
    """Test case for get_notifications_display_by_id_notification

    getNotificationsDisplayByIdNotification()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/display'.format(id_notification='id_notification_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_entities_by_id_notification(client):
    """Test case for get_notifications_entities_by_id_notification

    getNotificationsEntitiesByIdNotification()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/entities'.format(id_notification='id_notification_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_list_by_id_notification(client):
    """Test case for get_notifications_list_by_id_notification

    getNotificationsListByIdNotification()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/list'.format(id_notification='id_notification_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_list_by_id_notification_by_field(client):
    """Test case for get_notifications_list_by_id_notification_by_field

    getNotificationsListByIdNotificationByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/list/{_field}'.format(id_notification='id_notification_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_member_by_id_notification(client):
    """Test case for get_notifications_member_by_id_notification

    getNotificationsMemberByIdNotification()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/member'.format(id_notification='id_notification_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_member_by_id_notification_by_field(client):
    """Test case for get_notifications_member_by_id_notification_by_field

    getNotificationsMemberByIdNotificationByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/member/{_field}'.format(id_notification='id_notification_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_member_creator_by_id_notification(client):
    """Test case for get_notifications_member_creator_by_id_notification

    getNotificationsMemberCreatorByIdNotification()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/memberCreator'.format(id_notification='id_notification_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_member_creator_by_id_notification_by_field(client):
    """Test case for get_notifications_member_creator_by_id_notification_by_field

    getNotificationsMemberCreatorByIdNotificationByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/memberCreator/{_field}'.format(id_notification='id_notification_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_organization_by_id_notification(client):
    """Test case for get_notifications_organization_by_id_notification

    getNotificationsOrganizationByIdNotification()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/organization'.format(id_notification='id_notification_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_organization_by_id_notification_by_field(client):
    """Test case for get_notifications_organization_by_id_notification_by_field

    getNotificationsOrganizationByIdNotificationByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/{id_notification}/organization/{_field}'.format(id_notification='id_notification_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_notifications_by_id_notification(client):
    """Test case for update_notifications_by_id_notification

    updateNotificationsByIdNotification()
    """
    body = openapi_server.Notifications()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/notifications/{id_notification}'.format(id_notification='id_notification_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_notifications_unread_by_id_notification(client):
    """Test case for update_notifications_unread_by_id_notification

    updateNotificationsUnreadByIdNotification()
    """
    body = openapi_server.NotificationsUnread()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/notifications/{id_notification}/unread'.format(id_notification='id_notification_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

