# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.incoming_transfer_notification_request import IncomingTransferNotificationRequest
from openapi_server.models.outgoing_transfer_notification_request import OutgoingTransferNotificationRequest


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_incoming_transfer_created(client):
    """Test case for post_balance_platform_incoming_transfer_created

    Incoming transfer created
    """
    incoming_transfer_notification_request = openapi_server.IncomingTransferNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.incomingTransfer.created',
        headers=headers,
        json=incoming_transfer_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_incoming_transfer_updated(client):
    """Test case for post_balance_platform_incoming_transfer_updated

    Incoming transfer updated
    """
    incoming_transfer_notification_request = openapi_server.IncomingTransferNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.incomingTransfer.updated',
        headers=headers,
        json=incoming_transfer_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_outgoing_transfer_created(client):
    """Test case for post_balance_platform_outgoing_transfer_created

    Outgoing transfer created
    """
    outgoing_transfer_notification_request = openapi_server.OutgoingTransferNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.outgoingTransfer.created',
        headers=headers,
        json=outgoing_transfer_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_balance_platform_outgoing_transfer_updated(client):
    """Test case for post_balance_platform_outgoing_transfer_updated

    Outgoing transfer updated
    """
    outgoing_transfer_notification_request = openapi_server.OutgoingTransferNotificationRequest()
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/balancePlatform.outgoingTransfer.updated',
        headers=headers,
        json=outgoing_transfer_notification_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

