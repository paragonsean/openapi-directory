# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.webhooks import Webhooks
from openapi_server.models.webhooks_active import WebhooksActive
from openapi_server.models.webhooks_callback_url import WebhooksCallbackURL
from openapi_server.models.webhooks_description import WebhooksDescription
from openapi_server.models.webhooks_id_model import WebhooksIdModel


pytestmark = pytest.mark.asyncio

async def test_add_webhooks(client):
    """Test case for add_webhooks

    addWebhooks()
    """
    body = openapi_server.Webhooks()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/webhooks',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_webhooks_by_id_webhook(client):
    """Test case for delete_webhooks_by_id_webhook

    deleteWebhooksByIdWebhook()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/webhooks/{id_webhook}'.format(id_webhook='id_webhook_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhooks_by_id_webhook(client):
    """Test case for get_webhooks_by_id_webhook

    getWebhooksByIdWebhook()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/webhooks/{id_webhook}'.format(id_webhook='id_webhook_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhooks_by_id_webhook_by_field(client):
    """Test case for get_webhooks_by_id_webhook_by_field

    getWebhooksByIdWebhookByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/webhooks/{id_webhook}/{_field}'.format(id_webhook='id_webhook_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhooks(client):
    """Test case for update_webhooks

    updateWebhooks()
    """
    body = openapi_server.Webhooks()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/webhooks/',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhooks_active_by_id_webhook(client):
    """Test case for update_webhooks_active_by_id_webhook

    updateWebhooksActiveByIdWebhook()
    """
    body = openapi_server.WebhooksActive()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/webhooks/{id_webhook}/active'.format(id_webhook='id_webhook_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhooks_by_id_webhook(client):
    """Test case for update_webhooks_by_id_webhook

    updateWebhooksByIdWebhook()
    """
    body = openapi_server.Webhooks()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/webhooks/{id_webhook}'.format(id_webhook='id_webhook_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhooks_callback_urlby_id_webhook(client):
    """Test case for update_webhooks_callback_urlby_id_webhook

    updateWebhooksCallbackURLByIdWebhook()
    """
    body = openapi_server.WebhooksCallbackURL()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/webhooks/{id_webhook}/callbackURL'.format(id_webhook='id_webhook_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhooks_description_by_id_webhook(client):
    """Test case for update_webhooks_description_by_id_webhook

    updateWebhooksDescriptionByIdWebhook()
    """
    body = openapi_server.WebhooksDescription()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/webhooks/{id_webhook}/description'.format(id_webhook='id_webhook_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhooks_id_model_by_id_webhook(client):
    """Test case for update_webhooks_id_model_by_id_webhook

    updateWebhooksIdModelByIdWebhook()
    """
    body = openapi_server.WebhooksIdModel()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/webhooks/{id_webhook}/idModel'.format(id_webhook='id_webhook_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

