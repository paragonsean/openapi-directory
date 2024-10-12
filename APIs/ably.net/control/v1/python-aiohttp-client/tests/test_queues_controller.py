# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.queue import Queue
from openapi_server.models.queue_response import QueueResponse


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_queues_get(client):
    """Test case for apps_app_id_queues_get

    Lists queues
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/apps/{app_id}/queues'.format(app_id='app_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_queues_post(client):
    """Test case for apps_app_id_queues_post

    Creates a queue
    """
    body = openapi_server.Queue()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/apps/{app_id}/queues'.format(app_id='app_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_app_id_queues_queue_id_delete(client):
    """Test case for apps_app_id_queues_queue_id_delete

    Deletes a queue
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/apps/{app_id}/queues/{queue_id}'.format(app_id='app_id_example', queue_id='queue_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

