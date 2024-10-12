# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.notification_preview import NotificationPreview


pytestmark = pytest.mark.asyncio

async def test_notifications_contributions_id_preview_get(client):
    """Test case for notifications_contributions_id_preview_get

    
    """
    params = [('message', 'message_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/1/notifications/contributions/{id}/preview'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

