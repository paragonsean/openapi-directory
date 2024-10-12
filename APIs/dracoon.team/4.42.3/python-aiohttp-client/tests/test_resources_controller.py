# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.avatar import Avatar
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.notification_scope_list import NotificationScopeList


pytestmark = pytest.mark.asyncio

async def test_request_subscription_scopes(client):
    """Test case for request_subscription_scopes

    Request list of subscription scopes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/resources/user/notifications/scopes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_user_avatar(client):
    """Test case for request_user_avatar

    Request user avatar
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/resources/users/{user_id}/avatar/{uuid}'.format(uuid='uuid_example', user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

