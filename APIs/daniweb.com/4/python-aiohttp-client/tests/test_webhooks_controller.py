# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.endpoint_delete_webhooks_id import EndpointDeleteWebhooksID
from openapi_server.models.endpoint_get_webhooks import EndpointGetWebhooks
from openapi_server.models.endpoint_post_webhooks import EndpointPostWebhooks


pytestmark = pytest.mark.asyncio

async def test_webhooks_get(client):
    """Test case for webhooks_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/webhooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_webhooks_iddelete(client):
    """Test case for webhooks_iddelete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/connect/api/v4/webhooks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_webhooks_post(client):
    """Test case for webhooks_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('bubbled', False)
    data.add_field('event', 'event_example')
    data.add_field('name', 'name_example')
    data.add_field('object_id', 56)
    data.add_field('uri', 'uri_example')
    response = await client.request(
        method='POST',
        path='/connect/api/v4/webhooks',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

