# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_page import BatchPage
from openapi_server.models.batch_request import BatchRequest
from openapi_server.models.call import Call
from openapi_server.models.call_broadcast import CallBroadcast
from openapi_server.models.call_broadcast_page import CallBroadcastPage
from openapi_server.models.call_broadcast_stats import CallBroadcastStats
from openapi_server.models.call_list import CallList
from openapi_server.models.call_page import CallPage
from openapi_server.models.call_recipient import CallRecipient
from openapi_server.models.call_recording import CallRecording
from openapi_server.models.call_recording_list import CallRecordingList
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.recipient import Recipient
from openapi_server.models.resource_id import ResourceId


pytestmark = pytest.mark.asyncio

async def test_add_call_broadcast_batch(client):
    """Test case for add_call_broadcast_batch

    Add batches to a call broadcast
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
        path='/v2/calls/broadcasts/{id}/batches'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_call_broadcast_recipients(client):
    """Test case for add_call_broadcast_recipients

    Add recipients to a call broadcast
    """
    body = {"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":7,"attributes":{"key":"attributes"}}
    params = [('fields', 'fields_example'),
                    ('strictValidation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/calls/broadcasts/{id}/recipients'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_archive_voice_broadcast(client):
    """Test case for archive_voice_broadcast

    Archive voice broadcast
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/calls/broadcasts/{id}/archive'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_call_broadcast(client):
    """Test case for create_call_broadcast

    Create a call broadcast
    """
    body = {"retryConfig":{"maxAttempts":1,"retryResults":["retryResults","retryResults"],"retryPhoneTypes":["retryPhoneTypes","retryPhoneTypes"],"minutesBetweenAttempts":1},"answeringMachineConfig":"AM_ONLY","dialplanXml":"dialplanXml","labels":["labels","labels"],"fromNumber":"fromNumber","sounds":{"liveSoundText":"liveSoundText","machineSoundId":6,"machineSoundTextVoice":"MALE1","transferSoundText":"transferSoundText","transferSoundTextVoice":"MALE1","dncSoundId":8,"liveSoundId":9,"dncDigit":"dncDigit","machineSoundText":"machineSoundText","transferDigit":"transferDigit","dncSoundTextVoice":"MALE1","liveSoundTextVoice":"MALE1","dncSoundText":"dncSoundText","transferNumber":"transferNumber","transferSoundId":3},"recipients":[{"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":7,"attributes":{"key":"attributes"}},{"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":7,"attributes":{"key":"attributes"}}],"schedules":[{"campaignId":1,"stopTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"timeZone":"timeZone","id":6,"daysOfWeek":["daysOfWeek","daysOfWeek"],"startDate":{"month":1,"year":4,"day":7},"startTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"stopDate":{"month":1,"year":4,"day":7}},{"campaignId":1,"stopTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"timeZone":"timeZone","id":6,"daysOfWeek":["daysOfWeek","daysOfWeek"],"startDate":{"month":1,"year":4,"day":7},"startTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"stopDate":{"month":1,"year":4,"day":7}}],"localTimeRestriction":{"endHour":9,"beginHour":2,"beginMinute":7,"enabled":True,"endMinute":3},"name":"name","resumeNextDay":True,"id":5,"lastModified":5,"maxActiveTransfers":4,"maxActive":2,"status":"TEST"}
    params = [('start', True),
                    ('strictValidation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/calls/broadcasts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_call_broadcasts(client):
    """Test case for find_call_broadcasts

    Find call broadcasts
    """
    params = [('fields', 'fields_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('label', 'label_example'),
                    ('name', 'name_example'),
                    ('running', True),
                    ('scheduled', True),
                    ('intervalBegin', 56),
                    ('intervalEnd', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/calls/broadcasts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_calls(client):
    """Test case for find_calls

    Find calls
    """
    params = [('fields', 'fields_example'),
                    ('limit', 100),
                    ('offset', 0),
                    ('id', [56]),
                    ('campaignId', 56),
                    ('batchId', 56),
                    ('fromNumber', 'from_number_example'),
                    ('toNumber', 'to_number_example'),
                    ('label', 'label_example'),
                    ('states', 'states_example'),
                    ('results', 'results_example'),
                    ('inbound', True),
                    ('intervalBegin', 56),
                    ('intervalEnd', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/calls',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call(client):
    """Test case for get_call

    Find a specific call
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/calls/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call_broadcast(client):
    """Test case for get_call_broadcast

    Find a specific call broadcast
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/calls/broadcasts/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call_broadcast_batches(client):
    """Test case for get_call_broadcast_batches

    Find batches in a call broadcast
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
        path='/v2/calls/broadcasts/{id}/batches'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call_broadcast_calls(client):
    """Test case for get_call_broadcast_calls

    Find calls in a call broadcast
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
        path='/v2/calls/broadcasts/{id}/calls'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call_broadcast_stats(client):
    """Test case for get_call_broadcast_stats

    Get statistics on call broadcast
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
        path='/v2/calls/broadcasts/{id}/stats'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call_recording(client):
    """Test case for get_call_recording

    Get call recording by id
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/calls/recordings/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call_recording_by_name(client):
    """Test case for get_call_recording_by_name

    Get call recording by name
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/calls/{id}/recordings/{name}'.format(id=56, name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call_recording_mp3(client):
    """Test case for get_call_recording_mp3

    Get call recording in mp3 format
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/calls/recordings/{id_mp}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call_recording_mp3_by_name(client):
    """Test case for get_call_recording_mp3_by_name

    Get call mp3 recording by name
    """
    headers = { 
        'Accept': 'audio/mpeg',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/calls/{id}/recordings/{name_mp}'.format(id=56, name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_call_recordings(client):
    """Test case for get_call_recordings

    Get call recordings for a call
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/calls/{id}/recordings'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_calls(client):
    """Test case for send_calls

    Send calls
    """
    body = {"transferMessageSoundId":5,"voice":"MALE1","contactId":0,"dialplanXml":"dialplanXml","transferMessage":"transferMessage","fromNumber":"fromNumber","machineMessage":"machineMessage","liveMessageSoundId":6,"phoneNumber":"phoneNumber","machineMessageSoundId":1,"transferDigit":"transferDigit","attributes":{"key":"attributes"},"liveMessage":"liveMessage","transferNumber":"transferNumber"}
    params = [('fields', 'fields_example'),
                    ('campaignId', 56),
                    ('defaultLiveMessage', 'default_live_message_example'),
                    ('defaultMachineMessage', 'default_machine_message_example'),
                    ('defaultLiveMessageSoundId', 56),
                    ('defaultMachineMessageSoundId', 56),
                    ('defaultVoice', 'default_voice_example'),
                    ('strictValidation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/calls',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_voice_broadcast(client):
    """Test case for start_voice_broadcast

    Start voice broadcast
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/calls/broadcasts/{id}/start'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_voice_broadcast(client):
    """Test case for stop_voice_broadcast

    Stop voice broadcast
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/calls/broadcasts/{id}/stop'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_toggle_call_broadcast_recipients_status(client):
    """Test case for toggle_call_broadcast_recipients_status

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
        path='/v2/calls/broadcasts/{id}/toggleRecipientsStatus'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_call_broadcast(client):
    """Test case for update_call_broadcast

    Update a call broadcast
    """
    body = {"retryConfig":{"maxAttempts":1,"retryResults":["retryResults","retryResults"],"retryPhoneTypes":["retryPhoneTypes","retryPhoneTypes"],"minutesBetweenAttempts":1},"answeringMachineConfig":"AM_ONLY","dialplanXml":"dialplanXml","labels":["labels","labels"],"fromNumber":"fromNumber","sounds":{"liveSoundText":"liveSoundText","machineSoundId":6,"machineSoundTextVoice":"MALE1","transferSoundText":"transferSoundText","transferSoundTextVoice":"MALE1","dncSoundId":8,"liveSoundId":9,"dncDigit":"dncDigit","machineSoundText":"machineSoundText","transferDigit":"transferDigit","dncSoundTextVoice":"MALE1","liveSoundTextVoice":"MALE1","dncSoundText":"dncSoundText","transferNumber":"transferNumber","transferSoundId":3},"recipients":[{"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":7,"attributes":{"key":"attributes"}},{"fromNumber":"fromNumber","phoneNumber":"phoneNumber","contactId":7,"attributes":{"key":"attributes"}}],"schedules":[{"campaignId":1,"stopTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"timeZone":"timeZone","id":6,"daysOfWeek":["daysOfWeek","daysOfWeek"],"startDate":{"month":1,"year":4,"day":7},"startTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"stopDate":{"month":1,"year":4,"day":7}},{"campaignId":1,"stopTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"timeZone":"timeZone","id":6,"daysOfWeek":["daysOfWeek","daysOfWeek"],"startDate":{"month":1,"year":4,"day":7},"startTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"stopDate":{"month":1,"year":4,"day":7}}],"localTimeRestriction":{"endHour":9,"beginHour":2,"beginMinute":7,"enabled":True,"endMinute":3},"name":"name","resumeNextDay":True,"id":5,"lastModified":5,"maxActiveTransfers":4,"maxActive":2,"status":"TEST"}
    params = [('strictValidation', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/calls/broadcasts/{id}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

