# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute_add200_response import AttributeAdd200Response
from openapi_server.models.attribute_delete200_response import AttributeDelete200Response
from openapi_server.models.product_image_update200_response import ProductImageUpdate200Response
from openapi_server.models.webhook_count200_response import WebhookCount200Response
from openapi_server.models.webhook_events200_response import WebhookEvents200Response
from openapi_server.models.webhook_list200_response import WebhookList200Response


pytestmark = pytest.mark.asyncio

async def test_webhook_count(client):
    """Test case for webhook_count

    
    """
    params = [('entity', 'entity_example'),
                    ('action', 'action_example'),
                    ('active', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/webhook.count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhook_create(client):
    """Test case for webhook_create

    
    """
    params = [('entity', 'entity_example'),
                    ('action', 'action_example'),
                    ('callback', 'param_callback_example'),
                    ('label', 'label_example'),
                    ('fields', 'force_all'),
                    ('active', True),
                    ('store_id', 'store_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/webhook.create.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhook_delete(client):
    """Test case for webhook_delete

    
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.1/webhook.delete.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhook_events(client):
    """Test case for webhook_events

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/webhook.events.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhook_list(client):
    """Test case for webhook_list

    
    """
    params = [('params', 'id,entity,action,callback'),
                    ('start', 0),
                    ('count', 10),
                    ('entity', 'entity_example'),
                    ('action', 'action_example'),
                    ('active', True),
                    ('ids', 'ids_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.1/webhook.list.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhook_update(client):
    """Test case for webhook_update

    
    """
    params = [('id', 'id_example'),
                    ('callback', 'param_callback_example'),
                    ('label', 'label_example'),
                    ('fields', 'fields_example'),
                    ('active', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1.1/webhook.update.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

