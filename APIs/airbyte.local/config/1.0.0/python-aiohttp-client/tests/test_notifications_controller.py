# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.notification import Notification
from openapi_server.models.notification_read import NotificationRead


pytestmark = pytest.mark.asyncio

async def test_try_notification_config(client):
    """Test case for try_notification_config

    Try sending a notifications
    """
    body = {"slackConfiguration":{"webhook":"webhook"},"customerioConfiguration":"{}","sendOnFailure":True,"sendOnSuccess":False,"notificationType":"slack"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/notifications/try',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

