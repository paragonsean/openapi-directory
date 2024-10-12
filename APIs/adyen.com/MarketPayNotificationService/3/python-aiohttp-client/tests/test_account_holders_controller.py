# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_holder_create_notification import AccountHolderCreateNotification
from openapi_server.models.account_holder_status_change_notification import AccountHolderStatusChangeNotification
from openapi_server.models.account_holder_store_status_change_notification import AccountHolderStoreStatusChangeNotification
from openapi_server.models.account_holder_upcoming_deadline_notification import AccountHolderUpcomingDeadlineNotification
from openapi_server.models.account_holder_update_notification import AccountHolderUpdateNotification
from openapi_server.models.account_holder_verification_notification import AccountHolderVerificationNotification
from openapi_server.models.notification_response import NotificationResponse


pytestmark = pytest.mark.asyncio

async def test_post_accountholdercreated(client):
    """Test case for post_accountholdercreated

    Account holder created
    """
    account_holder_create_notification = openapi_server.AccountHolderCreateNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_HOLDER_CREATED',
        headers=headers,
        json=account_holder_create_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_accountholderstatuschange(client):
    """Test case for post_accountholderstatuschange

    Account holder status changed
    """
    account_holder_status_change_notification = openapi_server.AccountHolderStatusChangeNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_HOLDER_STATUS_CHANGE',
        headers=headers,
        json=account_holder_status_change_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_accountholderstorestatuschange(client):
    """Test case for post_accountholderstorestatuschange

    Store status changed
    """
    account_holder_store_status_change_notification = openapi_server.AccountHolderStoreStatusChangeNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_HOLDER_STORE_STATUS_CHANGE',
        headers=headers,
        json=account_holder_store_status_change_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_accountholderupcomingdeadline(client):
    """Test case for post_accountholderupcomingdeadline

    Upcoming deadline
    """
    account_holder_upcoming_deadline_notification = openapi_server.AccountHolderUpcomingDeadlineNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_HOLDER_UPCOMING_DEADLINE',
        headers=headers,
        json=account_holder_upcoming_deadline_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_accountholderupdated(client):
    """Test case for post_accountholderupdated

    Account holder updated
    """
    account_holder_update_notification = openapi_server.AccountHolderUpdateNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_HOLDER_UPDATED',
        headers=headers,
        json=account_holder_update_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_accountholderverification(client):
    """Test case for post_accountholderverification

    Verification results received
    """
    account_holder_verification_notification = openapi_server.AccountHolderVerificationNotification()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/ACCOUNT_HOLDER_VERIFICATION',
        headers=headers,
        json=account_holder_verification_notification,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

