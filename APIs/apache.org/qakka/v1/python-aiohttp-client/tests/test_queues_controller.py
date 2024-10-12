# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response import ApiResponse


pytestmark = pytest.mark.asyncio

async def test_ack_message(client):
    """Test case for ack_message

    Acknowledge that Queue Message has been processed.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/queues/{queue_name}/messages/{queue_message_id}'.format(queue_name='queue_name_example', queue_message_id='queue_message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_queue(client):
    """Test case for create_queue

    Create new queue.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/queues',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_queue(client):
    """Test case for delete_queue

    Delete Queue.
    """
    params = [('confirm', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/queues/{queue_name}'.format(queue_name='queue_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_of_queues(client):
    """Test case for get_list_of_queues

    Get list of all Queues.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/queues',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_message_data(client):
    """Test case for get_message_data

    Get data associated with a Queue Message.
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/queues/{queue_name}/data/{queue_message_id}'.format(queue_name='queue_name_example', queue_message_id='queue_message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_next_messages(client):
    """Test case for get_next_messages

    Get next Queue Messages from a Queue
    """
    params = [('count', '1')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/queues/{queue_name}/messages'.format(queue_name='queue_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_queue_config(client):
    """Test case for get_queue_config

    Get Queue config.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/queues/{queue_name}/config'.format(queue_name='queue_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_send_message_binary(client):
    """Test case for send_message_binary

    Send Queue Message with a binary data (blob) payload.
    """
    body = ['body_example']
    params = [('regions', 'regions_example'),
                    ('delay', 'delay_example'),
                    ('expiration', 'expiration_example'),
                    ('contentType', 'content_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='POST',
        path='/queues/{queue_name}/messages'.format(queue_name='queue_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_queue_config(client):
    """Test case for update_queue_config

    Update Queue configuration.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/queues/{queue_name}/config'.format(queue_name='queue_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

