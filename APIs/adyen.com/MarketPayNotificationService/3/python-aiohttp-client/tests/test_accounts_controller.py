# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_close_notification import AccountCloseNotification
from openapi_server.models.account_create_notification import AccountCreateNotification
from openapi_server.models.account_update_notification import AccountUpdateNotification
from openapi_server.models.notification_response import NotificationResponse


pytestmark = pytest.mark.asyncio

async def test_post_accountclosed(client):
    """Test case for post_accountclosed

    Account closed
    """
    account_close_notification = openapi_server.AccountCloseNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_CLOSED',
        headers=headers,
        json=account_close_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_accountcreated(client):
    """Test case for post_accountcreated

    Account created
    """
    account_create_notification = openapi_server.AccountCreateNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_CREATED',
        headers=headers,
        json=account_create_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_accountupdated(client):
    """Test case for post_accountupdated

    Account updated
    """
    account_update_notification = openapi_server.AccountUpdateNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_UPDATED',
        headers=headers,
        json=account_update_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

