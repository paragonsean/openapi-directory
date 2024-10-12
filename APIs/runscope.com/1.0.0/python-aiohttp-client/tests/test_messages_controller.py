# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.buckets_bucket_key_messages_post200_response import BucketsBucketKeyMessagesPost200Response
from openapi_server.models.error import Error
from openapi_server.models.new_message import NewMessage


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_errors_get(client):
    """Test case for buckets_bucket_key_errors_get

    Retrieve a list of error messages in a bucket
    """
    params = [('count', 56),
                    ('since', 56),
                    ('before', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buckets/{bucket_key}/errors'.format(bucket_key='bucket_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_messages_delete(client):
    """Test case for buckets_bucket_key_messages_delete

    Clear a bucket (remove all messages).
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/buckets/{bucket_key}/messages'.format(bucket_key='bucket_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_messages_get(client):
    """Test case for buckets_bucket_key_messages_get

    Retrieve a list of messages in a bucket
    """
    params = [('count', 56),
                    ('since', 56),
                    ('before', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buckets/{bucket_key}/messages'.format(bucket_key='bucket_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_buckets_bucket_key_messages_message_id_get(client):
    """Test case for buckets_bucket_key_messages_message_id_get

    Retrieve the details for a single message.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buckets/{bucket_key}/messages/{message_id}'.format(bucket_key='bucket_key_example', message_id='message_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_buckets_bucket_key_messages_post(client):
    """Test case for buckets_bucket_key_messages_post

    Create a message
    """
    new_message = openapi_server.NewMessage()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/buckets/{bucket_key}/messages'.format(bucket_key='bucket_key_example'),
        headers=headers,
        json=new_message,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

