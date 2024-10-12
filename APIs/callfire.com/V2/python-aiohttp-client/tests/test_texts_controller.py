# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_page import BatchPage
from openapi_server.models.batch_request import BatchRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.recipient import Recipient
from openapi_server.models.resource_id import ResourceId
from openapi_server.models.text import Text
from openapi_server.models.text_auto_reply import TextAutoReply
from openapi_server.models.text_auto_reply_page import TextAutoReplyPage
from openapi_server.models.text_broadcast import TextBroadcast
from openapi_server.models.text_broadcast_create_response import TextBroadcastCreateResponse
from openapi_server.models.text_broadcast_page import TextBroadcastPage
from openapi_server.models.text_broadcast_stats_dto import TextBroadcastStatsDto
from openapi_server.models.text_list import TextList
from openapi_server.models.text_page import TextPage
from openapi_server.models.text_recipient import TextRecipient


pytestmark = pytest.mark.asyncio

async def test_add_text_broadcast_batch(client):
    """Test case for add_text_broadcast_batch

    Add batches to a text broadcast
    """
    body = {"scrubDuplicates":True,"recipients":[{"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":7,"attributes":{"key":"attributes"}},{"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":7,"attributes":{"key":"attributes"}}],"contactListId":0,"name":"name"}
    params = [('strictValidation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/texts/broadcasts/{id}/batches'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_text_broadcast_recipients(client):
    """Test case for add_text_broadcast_recipients

    Add recipients to a text broadcast
    """
    body = {"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":0,"attributes":{"key":"attributes"},"media":[{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9},{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9}],"message":"message"}
    params = [('fields', 'fields_example'),
                    ('strictValidation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/texts/broadcasts/{id}/recipients'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_archive_text_broadcast(client):
    """Test case for archive_text_broadcast

    Archive text broadcast
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/texts/broadcasts/{id}/archive'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_text_auto_reply(client):
    """Test case for create_text_auto_reply

    Create an auto reply
    """
    body = {"number":"number","match":"match","id":5,"keyword":"keyword","message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/texts/auto-replys',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_text_broadcast(client):
    """Test case for create_text_broadcast

    Create a text broadcast
    """
    body = {"bigMessageStrategy":"SEND_MULTIPLE","media":[{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9},{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9}],"message":"message","labels":["labels","labels"],"fromNumber":"fromNumber","recipients":[{"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":0,"attributes":{"key":"attributes"},"media":[{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9},{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9}],"message":"message"},{"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":0,"attributes":{"key":"attributes"},"media":[{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9},{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9}],"message":"message"}],"schedules":[{"campaignId":1,"stopTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"timeZone":"timeZone","id":6,"daysOfWeek":["daysOfWeek","daysOfWeek"],"startDate":{"month":1,"year":4,"day":7},"startTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"stopDate":{"month":1,"year":4,"day":7}},{"campaignId":1,"stopTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"timeZone":"timeZone","id":6,"daysOfWeek":["daysOfWeek","daysOfWeek"],"startDate":{"month":1,"year":4,"day":7},"startTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"stopDate":{"month":1,"year":4,"day":7}}],"localTimeRestriction":{"endHour":9,"beginHour":2,"beginMinute":7,"enabled":True,"endMinute":3},"name":"name","resumeNextDay":True,"id":5,"lastModified":5,"maxActive":2,"status":"TEST"}
    params = [('start', True),
                    ('strictValidation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/texts/broadcasts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_text_auto_reply(client):
    """Test case for delete_text_auto_reply

    Delete an auto reply
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/texts/auto-replys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_text_auto_replys(client):
    """Test case for find_text_auto_replys

    Find auto replies
    """
    params = [('fields', 'fields_example'),
                    ('limit', 100),
                    ('offset', 0),
                    ('number', 'number_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/texts/auto-replys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_text_broadcasts(client):
    """Test case for find_text_broadcasts

    Find text broadcasts
    """
    params = [('name', 'name_example'),
                    ('label', 'label_example'),
                    ('running', True),
                    ('scheduled', True),
                    ('intervalBegin', 56),
                    ('intervalEnd', 56),
                    ('limit', 10),
                    ('offset', 0),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/texts/broadcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_texts(client):
    """Test case for find_texts

    Find texts
    """
    params = [('id', [56]),
                    ('campaignId', 56),
                    ('batchId', 56),
                    ('fromNumber', 'from_number_example'),
                    ('toNumber', 'to_number_example'),
                    ('label', 'label_example'),
                    ('states', 'states_example'),
                    ('results', 'results_example'),
                    ('inbound', True),
                    ('intervalBegin', 56),
                    ('intervalEnd', 56),
                    ('limit', 10),
                    ('offset', 0),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/texts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text(client):
    """Test case for get_text

    Find a specific text
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/texts/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_auto_reply(client):
    """Test case for get_text_auto_reply

    Find a specific auto reply
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/texts/auto-replys/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_broadcast(client):
    """Test case for get_text_broadcast

    Find a specific text broadcast
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/texts/broadcasts/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_broadcast_batches(client):
    """Test case for get_text_broadcast_batches

    Find batches in a text broadcast
    """
    params = [('fields', 'fields_example'),
                    ('limit', 100),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/texts/broadcasts/{id}/batches'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_broadcast_stats(client):
    """Test case for get_text_broadcast_stats

    Get statistics on text broadcast
    """
    params = [('fields', 'fields_example'),
                    ('begin', 56),
                    ('end', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/texts/broadcasts/{id}/stats'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_text_broadcast_texts(client):
    """Test case for get_text_broadcast_texts

    Find texts in a text broadcast
    """
    params = [('batchId', 56),
                    ('fields', 'fields_example'),
                    ('limit', 100),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/texts/broadcasts/{id}/texts'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_texts(client):
    """Test case for send_texts

    Send texts
    """
    body = {"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":0,"attributes":{"key":"attributes"},"media":[{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9},{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9}],"message":"message"}
    params = [('fields', 'fields_example'),
                    ('campaignId', 56),
                    ('defaultMessage', 'default_message_example'),
                    ('strictValidation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/texts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_text_broadcast(client):
    """Test case for start_text_broadcast

    Start text broadcast
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/texts/broadcasts/{id}/start'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_text_broadcast(client):
    """Test case for stop_text_broadcast

    Stop text broadcast
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/texts/broadcasts/{id}/stop'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_toggle_text_broadcast_recipients_status(client):
    """Test case for toggle_text_broadcast_recipients_status

    Disable/enable undialed recipients in broadcast
    """
    body = {"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":7,"attributes":{"key":"attributes"}}
    params = [('enable', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/texts/broadcasts/{id}/toggleRecipientsStatus'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_text_broadcast(client):
    """Test case for update_text_broadcast

    Update a text broadcast
    """
    body = {"bigMessageStrategy":"SEND_MULTIPLE","media":[{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9},{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9}],"message":"message","labels":["labels","labels"],"fromNumber":"fromNumber","recipients":[{"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":0,"attributes":{"key":"attributes"},"media":[{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9},{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9}],"message":"message"},{"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":0,"attributes":{"key":"attributes"},"media":[{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9},{"accountId":2,"lengthInBytes":3,"created":7,"name":"name","publicUrl":"publicUrl","mediaType":"mediaType","id":9}],"message":"message"}],"schedules":[{"campaignId":1,"stopTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"timeZone":"timeZone","id":6,"daysOfWeek":["daysOfWeek","daysOfWeek"],"startDate":{"month":1,"year":4,"day":7},"startTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"stopDate":{"month":1,"year":4,"day":7}},{"campaignId":1,"stopTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"timeZone":"timeZone","id":6,"daysOfWeek":["daysOfWeek","daysOfWeek"],"startDate":{"month":1,"year":4,"day":7},"startTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"stopDate":{"month":1,"year":4,"day":7}}],"localTimeRestriction":{"endHour":9,"beginHour":2,"beginMinute":7,"enabled":True,"endMinute":3},"name":"name","resumeNextDay":True,"id":5,"lastModified":5,"maxActive":2,"status":"TEST"}
    params = [('strictValidation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/texts/broadcasts/{id}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

