# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_bulk_message_result import CreateBulkMessageResult
from openapi_server.models.create_message import CreateMessage
from openapi_server.models.create_message_result import CreateMessageResult
from openapi_server.models.message import Message
from openapi_server.models.messages_result import MessagesResult
from openapi_server.models.search import Search


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_messages_create(client):
    """Test case for messages_create

    Create a new message.
    """
    body = {"dateTime":"2000-01-23T04:56:07.000+00:00","severity":"severity","code":"code","data":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"method":"method","source":"source","queryString":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"title":"title","type":"type","version":"version","cookies":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"url":"url","hostname":"hostname","application":"application","form":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"serverVariables":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"correlationId":"correlationId","detail":"detail","category":"category","user":"user","breadcrumbs":[{"dateTime":"2000-01-23T04:56:07.000+00:00","severity":"severity","action":"action","message":"message"},{"dateTime":"2000-01-23T04:56:07.000+00:00","severity":"severity","action":"action","message":"message"}],"statusCode":0,"titleTemplate":"titleTemplate"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/messages/{log_id}'.format(log_id='log_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_messages_create_bulk(client):
    """Test case for messages_create_bulk

    Create one or more new messages.
    """
    body = {"dateTime":"2000-01-23T04:56:07.000+00:00","severity":"severity","code":"code","data":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"method":"method","source":"source","queryString":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"title":"title","type":"type","version":"version","cookies":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"url":"url","hostname":"hostname","application":"application","form":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"serverVariables":[{"value":"value","key":"key"},{"value":"value","key":"key"}],"correlationId":"correlationId","detail":"detail","category":"category","user":"user","breadcrumbs":[{"dateTime":"2000-01-23T04:56:07.000+00:00","severity":"severity","action":"action","message":"message"},{"dateTime":"2000-01-23T04:56:07.000+00:00","severity":"severity","action":"action","message":"message"}],"statusCode":0,"titleTemplate":"titleTemplate"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/messages/{log_id}/_bulk'.format(log_id='log_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_delete(client):
    """Test case for messages_delete

    Delete a message by its ID.
    """
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/messages/{log_id}/{id}'.format(id='id_example', log_id='log_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_messages_delete_all(client):
    """Test case for messages_delete_all

    Deletes a list of messages by logid and query.
    """
    body = {"query":"query","from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Content-Type': 'application/*+json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/messages/{log_id}'.format(log_id='log_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_fix(client):
    """Test case for messages_fix

    Fix a message by its ID.
    """
    params = [('markAllAsFixed', False)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/messages/{log_id}/{id}/_fix'.format(id='id_example', log_id='log_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_messages_fix_all(client):
    """Test case for messages_fix_all

    Mark a list of messages as fixed by logid and query.
    """
    body = {"query":"query","from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Content-Type': 'application/*+json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/messages/{log_id}/_fix'.format(log_id='log_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_get(client):
    """Test case for messages_get

    Fetch a message by its ID.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/messages/{log_id}/{id}'.format(id='id_example', log_id='log_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_get_all(client):
    """Test case for messages_get_all

    Fetch messages from a log.
    """
    params = [('pageIndex', 0),
                    ('pageSize', 15),
                    ('query', 'query_example'),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('includeHeaders', False)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/messages/{log_id}'.format(log_id='log_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_hide(client):
    """Test case for messages_hide

    Hide a message by its ID.
    """
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/messages/{log_id}/{id}/_hide'.format(id='id_example', log_id='log_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

