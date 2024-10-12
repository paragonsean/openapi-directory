# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_notification_request_body import AddNotificationRequestBody
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.notification_collection_response import NotificationCollectionResponse
from openapi_server.models.notification_response import NotificationResponse
from openapi_server.models.update_notification_by_id_request_body import UpdateNotificationByIdRequestBody


pytestmark = pytest.mark.asyncio

async def test_add_notification(client):
    """Test case for add_notification

    Create a new notification
    """
    body = {"sendEmail":True,"resource":"resource","recipients":["myemail@example.com"],"action":"upload","usernames":["usernames","usernames"],"message":"message","type":"file"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/notifications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_notification_by_id(client):
    """Test case for delete_notification_by_id

    Delete a notification
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/notifications/{id}'.format(id=3),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notification_by_id(client):
    """Test case for get_notification_by_id

    Get notification details
    """
    params = [('include', 'resource,share')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/notifications/{id}'.format(id=3),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_notifications(client):
    """Test case for list_notifications

    Get a list of notifications
    """
    params = [('type', 'file'),
                    ('offset', 0),
                    ('sort', 'date'),
                    ('limit', 25),
                    ('include', 'resource,share,user'),
                    ('action', 'all')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_notification_by_id(client):
    """Test case for update_notification_by_id

    Update a notification
    """
    body = {"sendEmail":True,"recipients":["myemail@example.com"],"action":"all","usernames":["notice_user_all"],"message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/notifications/{id}'.format(id=3),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

