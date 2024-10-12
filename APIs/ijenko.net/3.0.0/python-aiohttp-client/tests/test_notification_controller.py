# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.notification import Notification
from openapi_server.models.notification_created import NotificationCreated
from openapi_server.models.notification_item import NotificationItem
from openapi_server.models.notification_new import NotificationNew
from openapi_server.models.notification_patch import NotificationPatch


pytestmark = pytest.mark.asyncio

async def test_notification_delete(client):
    """Test case for notification_delete

    Delete a Notification
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/notifications/{notification_id}'.format(notification_id='notification_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_get_metadata(client):
    """Test case for notification_get_metadata

    List metadata
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/notifications/{notification_id}/metadata'.format(notification_id='notification_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_patch(client):
    """Test case for notification_patch

    Modify a Notification
    """
    notification_patch = {"routing":"https://openapi-generator.tech","data":"{}","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/notifications/{notification_id}'.format(notification_id='notification_id_example'),
        headers=headers,
        json=notification_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_patch_metadata(client):
    """Test case for notification_patch_metadata

    Modify metadata of a Notification
    """
    metadata_patch = {"add":{},"remove":[null,null]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/notifications/{notification_id}/metadata'.format(notification_id='notification_id_example'),
        headers=headers,
        json=metadata_patch,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notifications_get(client):
    """Test case for notifications_get

    Information about a Notification
    """
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/notifications/{notification_id}'.format(notification_id='notification_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_new_notification(client):
    """Test case for place_new_notification

    Create a Notification
    """
    notification = {"routing":"https://openapi-generator.tech","metadata":{},"data":"{}","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/places/{place_id}/notifications'.format(place_id='place_id_example'),
        headers=headers,
        json=notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_place_notifications(client):
    """Test case for place_notifications

    List Notifications
    """
    params = [('embed-metadata', ['embed_metadata_example'])]
    headers = { 
        'Accept': 'application/json',
        'Token in query': 'special-key',
        'Token in Access-Token header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/places/{place_id}/notifications'.format(place_id='place_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

