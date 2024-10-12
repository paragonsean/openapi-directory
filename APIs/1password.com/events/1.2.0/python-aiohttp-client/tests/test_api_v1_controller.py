# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.audit_event_items import AuditEventItems
from openapi_server.models.error import Error
from openapi_server.models.item_usage_items import ItemUsageItems
from openapi_server.models.sign_in_attempt_items import SignInAttemptItems


pytestmark = pytest.mark.asyncio

async def test_get_audit_events(client):
    """Test case for get_audit_events

    Retrieves audit events for actions performed by team members within a 1Password account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auditevents',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item_usages(client):
    """Test case for get_item_usages

    Retrieves events for each usage of an item stored in a shared vault within a 1Password account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/itemusages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sign_in_attempts(client):
    """Test case for get_sign_in_attempts

    Retrieves events for both successful and failed attempts to sign into a 1Password account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/signinattempts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

