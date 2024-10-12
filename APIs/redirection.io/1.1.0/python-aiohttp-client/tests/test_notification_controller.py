# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_read import NotificationRead


pytestmark = pytest.mark.asyncio

async def test_get_notification_collection(client):
    """Test case for get_notification_collection

    Retrieves the collection of Notification resources.
    """
    params = [('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notification_item(client):
    """Test case for get_notification_item

    Retrieves a Notification resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/notifications/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

