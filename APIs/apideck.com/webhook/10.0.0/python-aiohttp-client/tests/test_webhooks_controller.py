# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_webhook_request import CreateWebhookRequest
from openapi_server.models.create_webhook_response import CreateWebhookResponse
from openapi_server.models.delete_webhook_response import DeleteWebhookResponse
from openapi_server.models.get_webhook_event_logs_response import GetWebhookEventLogsResponse
from openapi_server.models.get_webhook_response import GetWebhookResponse
from openapi_server.models.get_webhooks_response import GetWebhooksResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_webhook_request import UpdateWebhookRequest
from openapi_server.models.update_webhook_response import UpdateWebhookResponse
from openapi_server.models.webhook_event_logs_filter import WebhookEventLogsFilter


pytestmark = pytest.mark.asyncio

async def test_event_logs_all(client):
    """Test case for event_logs_all

    List event logs
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.WebhookEventLogsFilter())]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/webhook/logs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_add(client):
    """Test case for webhooks_add

    Create webhook subscription
    """
    body = {"description":"A description","delivery_url":"https://example.com/my/webhook/endpoint","events":["vault.connection.created","vault.connection.updated"],"unified_api":"crm","status":"enabled"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/webhook/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_all(client):
    """Test case for webhooks_all

    List webhook subscriptions
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 20)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/webhook/webhooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_delete(client):
    """Test case for webhooks_delete

    Delete webhook subscription
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/webhook/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_one(client):
    """Test case for webhooks_one

    Get webhook subscription
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/webhook/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_update(client):
    """Test case for webhooks_update

    Update webhook subscription
    """
    body = {"description":"A description","delivery_url":"https://example.com/my/webhook/endpoint","events":["vault.connection.created","vault.connection.updated"],"status":"enabled"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/webhook/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

