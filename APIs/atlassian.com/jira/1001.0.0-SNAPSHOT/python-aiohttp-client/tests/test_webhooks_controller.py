# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.container_for_registered_webhooks import ContainerForRegisteredWebhooks
from openapi_server.models.container_for_webhook_ids import ContainerForWebhookIDs
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.failed_webhooks import FailedWebhooks
from openapi_server.models.page_bean_webhook import PageBeanWebhook
from openapi_server.models.webhook_registration_details import WebhookRegistrationDetails
from openapi_server.models.webhooks_expiration_date import WebhooksExpirationDate


pytestmark = pytest.mark.asyncio

async def test_delete_webhook_by_id(client):
    """Test case for delete_webhook_by_id

    Delete webhooks by ID
    """
    body = {"webhookIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/webhook',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dynamic_webhooks_for_app(client):
    """Test case for get_dynamic_webhooks_for_app

    Get dynamic webhooks for app
    """
    params = [('startAt', 0),
                    ('maxResults', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/webhook',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_failed_webhooks(client):
    """Test case for get_failed_webhooks

    Get failed webhooks
    """
    params = [('maxResults', 56),
                    ('after', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/webhook/failed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refresh_webhooks(client):
    """Test case for refresh_webhooks

    Extend webhook life
    """
    body = {"webhookIds":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/webhook/refresh',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_dynamic_webhooks(client):
    """Test case for register_dynamic_webhooks

    Register dynamic webhooks
    """
    body = {"webhooks":[{"jqlFilter":"jqlFilter","fieldIdsFilter":["fieldIdsFilter","fieldIdsFilter"],"issuePropertyKeysFilter":["issuePropertyKeysFilter","issuePropertyKeysFilter"],"events":["jira:issue_created","jira:issue_created"]},{"jqlFilter":"jqlFilter","fieldIdsFilter":["fieldIdsFilter","fieldIdsFilter"],"issuePropertyKeysFilter":["issuePropertyKeysFilter","issuePropertyKeysFilter"],"events":["jira:issue_created","jira:issue_created"]}],"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/webhook',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

