# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.bundle_notification_entity import BundleNotificationEntity


pytestmark = pytest.mark.asyncio

async def test_delete_bundle_notifications_id(client):
    """Test case for delete_bundle_notifications_id

    Delete Bundle Notification
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/bundle_notifications/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bundle_notifications(client):
    """Test case for get_bundle_notifications

    List Bundle Notifications
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('bundle_id', 'bundle_id_example'),
                    ('filter', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/bundle_notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bundle_notifications_id(client):
    """Test case for get_bundle_notifications_id

    Show Bundle Notification
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/bundle_notifications/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_bundle_notifications_id(client):
    """Test case for patch_bundle_notifications_id

    Update Bundle Notification
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('notify_on_registration', True)
    data.add_field('notify_on_upload', True)
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/bundle_notifications/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_bundle_notifications(client):
    """Test case for post_bundle_notifications

    Create Bundle Notification
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('bundle_id', 56)
    data.add_field('notify_on_registration', True)
    data.add_field('notify_on_upload', True)
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/bundle_notifications',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

