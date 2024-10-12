# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.webhook_instance import WebhookInstance


pytestmark = pytest.mark.asyncio

async def test_delete_webhook_instance(client):
    """Test case for delete_webhook_instance

    DELETE a WebhookInstance
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/webhook_instances/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhook_instances(client):
    """Test case for get_webhook_instances

    GET a WebhookInstance
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/webhook_instances/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

