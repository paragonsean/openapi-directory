# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.permission import Permission


pytestmark = pytest.mark.asyncio

async def test_permissions_delete(client):
    """Test case for permissions_delete

    Unlink an Object from another Object
    """
    body = {"attributeId":0,"calendarId":6,"driverId":5,"managedUserId":7,"groupId":2,"notificationId":9,"geofenceId":5,"deviceId":1,"userId":3}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/permissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_permissions_post(client):
    """Test case for permissions_post

    Link an Object to another Object
    """
    body = {"attributeId":0,"calendarId":6,"driverId":5,"managedUserId":7,"groupId":2,"notificationId":9,"geofenceId":5,"deviceId":1,"userId":3}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/permissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

