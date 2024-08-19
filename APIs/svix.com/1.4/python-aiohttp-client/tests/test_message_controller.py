# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_message_out import ListResponseMessageOut
from openapi_server.models.message_in import MessageIn
from openapi_server.models.message_out import MessageOut


pytestmark = pytest.mark.asyncio

async def test_create_message_api_v1_app_app_id_msg_post(client):
    """Test case for create_message_api_v1_app_app_id_msg_post

    Create Message
    """
    body = {"eventId":"evt_pNZKtWg8Azow","payloadRetentionPeriod":90,"application":{"uid":"unique-app-identifier","metadata":{"key":"metadata"},"rateLimit":1000,"name":"My first application"},"channels":["project_123","group_2"],"payload":{"email":"test@example.com","username":"test_user"},"eventType":"user.signup"}
    params = [('with_content', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/app/{app_id}/msg'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expunge_message_payload_api_v1_app_app_id_msg_msg_id_content_delete(client):
    """Test case for expunge_message_payload_api_v1_app_app_id_msg_msg_id_content_delete

    Delete message payload
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/app/{app_id}/msg/{msg_id}/content'.format(msg_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_message_api_v1_app_app_id_msg_msg_id_get(client):
    """Test case for get_message_api_v1_app_app_id_msg_msg_id_get

    Get Message
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/msg/{msg_id}'.format(msg_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_messages_api_v1_app_app_id_msg_get(client):
    """Test case for list_messages_api_v1_app_app_id_msg_get

    List Messages
    """
    params = [('iterator', 'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50),
                    ('event_types', ['event_types_example']),
                    ('channel', 'project_1337'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('after', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/msg'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

