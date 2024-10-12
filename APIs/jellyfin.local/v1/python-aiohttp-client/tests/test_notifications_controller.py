# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.name_id_pair import NameIdPair
from openapi_server.models.notification_level import NotificationLevel
from openapi_server.models.notification_result_dto import NotificationResultDto
from openapi_server.models.notification_type_info import NotificationTypeInfo
from openapi_server.models.notifications_summary_dto import NotificationsSummaryDto


pytestmark = pytest.mark.asyncio

async def test_create_admin_notification(client):
    """Test case for create_admin_notification

    Sends a notification to all admins.
    """
    params = [('url', 'url_example'),
                    ('level', openapi_server.NotificationLevel()),
                    ('name', ''),
                    ('description', '')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Notifications/Admin',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notification_services(client):
    """Test case for get_notification_services

    Gets notification services.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Notifications/Services',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notification_types(client):
    """Test case for get_notification_types

    Gets notification types.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Notifications/Types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications(client):
    """Test case for get_notifications

    Gets a user's notifications.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Notifications/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_summary(client):
    """Test case for get_notifications_summary

    Gets a user's notification summary.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Notifications/{user_id}/Summary'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_read(client):
    """Test case for set_read

    Sets notifications as read.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Notifications/{user_id}/Read'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_unread(client):
    """Test case for set_unread

    Sets notifications as unread.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Notifications/{user_id}/Unread'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

