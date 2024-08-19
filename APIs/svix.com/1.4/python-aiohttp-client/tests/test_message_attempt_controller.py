# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_endpoint_message_out import ListResponseEndpointMessageOut
from openapi_server.models.list_response_message_attempt_endpoint_out import ListResponseMessageAttemptEndpointOut
from openapi_server.models.list_response_message_attempt_out import ListResponseMessageAttemptOut
from openapi_server.models.list_response_message_endpoint_out import ListResponseMessageEndpointOut
from openapi_server.models.message_attempt_out import MessageAttemptOut
from openapi_server.models.message_status import MessageStatus
from openapi_server.models.status_code_class import StatusCodeClass


pytestmark = pytest.mark.asyncio

async def test_expunge_attempt_content_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_content_delete(client):
    """Test case for expunge_attempt_content_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_content_delete

    Delete attempt response body
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/app/{app_id}/msg/{msg_id}/attempt/{attempt_id}/content'.format(attempt_id='atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2', msg_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_attempt_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_get(client):
    """Test case for get_attempt_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_get

    Get Attempt
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/msg/{msg_id}/attempt/{attempt_id}'.format(attempt_id='atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2', msg_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_attempted_destinations_api_v1_app_app_id_msg_msg_id_endpoint_get(client):
    """Test case for list_attempted_destinations_api_v1_app_app_id_msg_msg_id_endpoint_get

    List Attempted Destinations
    """
    params = [('iterator', 'msgep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/msg/{msg_id}/endpoint'.format(msg_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_attempted_messages_api_v1_app_app_id_endpoint_endpoint_id_msg_get(client):
    """Test case for list_attempted_messages_api_v1_app_app_id_endpoint_endpoint_id_msg_get

    List Attempted Messages
    """
    params = [('iterator', 'msg_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50),
                    ('channel', 'project_1337'),
                    ('status', openapi_server.MessageStatus()),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('after', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/endpoint/{endpoint_id}/msg'.format(endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_attempts_api_v1_app_app_id_msg_msg_id_attempt_get(client):
    """Test case for list_attempts_api_v1_app_app_id_msg_msg_id_attempt_get

    List Attempts
    """
    params = [('iterator', 'atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50),
                    ('endpoint_id', 'ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('event_types', ['event_types_example']),
                    ('channel', 'project_1337'),
                    ('status', openapi_server.MessageStatus()),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('after', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/msg/{msg_id}/attempt'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2', msg_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_attempts_by_endpoint_api_v1_app_app_id_attempt_endpoint_endpoint_id_get(client):
    """Test case for list_attempts_by_endpoint_api_v1_app_app_id_attempt_endpoint_endpoint_id_get

    List Attempts By Endpoint
    """
    params = [('iterator', 'atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50),
                    ('status', openapi_server.MessageStatus()),
                    ('status_code_class', openapi_server.StatusCodeClass()),
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
        path='/api/v1/app/{app_id}/attempt/endpoint/{endpoint_id}'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2', endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_attempts_by_msg_api_v1_app_app_id_attempt_msg_msg_id_get(client):
    """Test case for list_attempts_by_msg_api_v1_app_app_id_attempt_msg_msg_id_get

    List Attempts By Msg
    """
    params = [('endpoint_id', 'ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('iterator', 'atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50),
                    ('status', openapi_server.MessageStatus()),
                    ('status_code_class', openapi_server.StatusCodeClass()),
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
        path='/api/v1/app/{app_id}/attempt/msg/{msg_id}'.format(app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2', msg_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_attempts_for_endpoint_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_attempt_get(client):
    """Test case for list_attempts_for_endpoint_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_attempt_get

    List Attempts For Endpoint
    """
    params = [('iterator', 'atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50),
                    ('event_types', ['event_types_example']),
                    ('channel', 'project_1337'),
                    ('status', openapi_server.MessageStatus()),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('after', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/app/{app_id}/msg/{msg_id}/endpoint/{endpoint_id}/attempt'.format(msg_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2', endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_webhook_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_resend_post(client):
    """Test case for resend_webhook_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_resend_post

    Resend Webhook
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/app/{app_id}/msg/{msg_id}/endpoint/{endpoint_id}/resend'.format(endpoint_id='ep_1srOrx2ZWZBpBUvZwXKQmoEYga2', msg_id='msg_1srOrx2ZWZBpBUvZwXKQmoEYga2', app_id='app_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

