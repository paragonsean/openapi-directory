# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.build_beta_notification_create_request import BuildBetaNotificationCreateRequest
from openapi_server.models.build_beta_notification_response import BuildBetaNotificationResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_build_beta_notifications_create_instance(client):
    """Test case for build_beta_notifications_create_instance

    
    """
    body = {"data":{"relationships":{"build":{"data":{"id":"id","type":"builds"}}},"type":"buildBetaNotifications"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/buildBetaNotifications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

