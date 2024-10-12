# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.notification_entity import NotificationEntity


pytestmark = pytest.mark.asyncio

async def test_delete_notifications_id(client):
    """Test case for delete_notifications_id

    Delete Notification
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/notifications/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications(client):
    """Test case for get_notifications

    List Notifications
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('group_id', 'group_id_example'),
                    ('filter', None),
                    ('filter_prefix', None),
                    ('path', 'path_example'),
                    ('include_ancestors', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_id(client):
    """Test case for get_notifications_id

    Show Notification
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/notifications/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_notifications_id(client):
    """Test case for patch_notifications_id

    Update Notification
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('message', 'message_example')
    data.add_field('notify_on_copy', True)
    data.add_field('notify_on_delete', True)
    data.add_field('notify_on_download', True)
    data.add_field('notify_on_move', True)
    data.add_field('notify_on_upload', True)
    data.add_field('notify_user_actions', True)
    data.add_field('recursive', True)
    data.add_field('send_interval', 'send_interval_example')
    data.add_field('trigger_by_share_recipients', True)
    data.add_field('triggering_filenames', ['triggering_filenames_example'])
    data.add_field('triggering_group_ids', [56])
    data.add_field('triggering_user_ids', [56])
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/notifications/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_notifications(client):
    """Test case for post_notifications

    Create Notification
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('group_id', 56)
    data.add_field('message', 'message_example')
    data.add_field('notify_on_copy', True)
    data.add_field('notify_on_delete', True)
    data.add_field('notify_on_download', True)
    data.add_field('notify_on_move', True)
    data.add_field('notify_on_upload', True)
    data.add_field('notify_user_actions', True)
    data.add_field('path', 'path_example')
    data.add_field('recursive', True)
    data.add_field('send_interval', 'send_interval_example')
    data.add_field('trigger_by_share_recipients', True)
    data.add_field('triggering_filenames', ['triggering_filenames_example'])
    data.add_field('triggering_group_ids', [56])
    data.add_field('triggering_user_ids', [56])
    data.add_field('user_id', 56)
    data.add_field('username', 'username_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/notifications',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

