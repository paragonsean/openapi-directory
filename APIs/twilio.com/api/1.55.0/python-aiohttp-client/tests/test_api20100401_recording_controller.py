# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_call_call_recording import ApiV2010AccountCallCallRecording
from openapi_server.models.api_v2010_account_conference_conference_recording import ApiV2010AccountConferenceConferenceRecording
from openapi_server.models.api_v2010_account_recording import ApiV2010AccountRecording
from openapi_server.models.call_recording_enum_status import CallRecordingEnumStatus
from openapi_server.models.conference_recording_enum_status import ConferenceRecordingEnumStatus
from openapi_server.models.list_call_recording_response import ListCallRecordingResponse
from openapi_server.models.list_conference_recording_response import ListConferenceRecordingResponse
from openapi_server.models.list_recording_response import ListRecordingResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_call_recording(client):
    """Test case for create_call_recording

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'recording_channels': 'recording_channels_example',
        'recording_status_callback': 'recording_status_callback_example',
        'recording_status_callback_event': ['recording_status_callback_event_example'],
        'recording_status_callback_method': 'recording_status_callback_method_example',
        'recording_track': 'recording_track_example',
        'trim': 'trim_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json'.format(account_sid='account_sid_example', call_sid='call_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_call_recording(client):
    """Test case for delete_call_recording

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid_jso}'.format(account_sid='account_sid_example', call_sid='call_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_conference_recording(client):
    """Test case for delete_conference_recording

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid_jso}'.format(account_sid='account_sid_example', conference_sid='conference_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_recording(client):
    """Test case for delete_recording

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Recordings/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_call_recording(client):
    """Test case for fetch_call_recording

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid_jso}'.format(account_sid='account_sid_example', call_sid='call_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_conference_recording(client):
    """Test case for fetch_conference_recording

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid_jso}'.format(account_sid='account_sid_example', conference_sid='conference_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_recording(client):
    """Test case for fetch_recording

    
    """
    params = [('IncludeSoftDeleted', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Recordings/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_call_recording(client):
    """Test case for list_call_recording

    
    """
    params = [('DateCreated', '2013-10-20'),
                    ('DateCreated&lt;', '2013-10-20'),
                    ('DateCreated&gt;', '2013-10-20'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings.json'.format(account_sid='account_sid_example', call_sid='call_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_conference_recording(client):
    """Test case for list_conference_recording

    
    """
    params = [('DateCreated', '2013-10-20'),
                    ('DateCreated&lt;', '2013-10-20'),
                    ('DateCreated&gt;', '2013-10-20'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings.json'.format(account_sid='account_sid_example', conference_sid='conference_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_recording(client):
    """Test case for list_recording

    
    """
    params = [('DateCreated', '2013-10-20T19:20:30+01:00'),
                    ('DateCreated&lt;', '2013-10-20T19:20:30+01:00'),
                    ('DateCreated&gt;', '2013-10-20T19:20:30+01:00'),
                    ('CallSid', 'call_sid_example'),
                    ('ConferenceSid', 'conference_sid_example'),
                    ('IncludeSoftDeleted', True),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Recordings.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_call_recording(client):
    """Test case for update_call_recording

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'pause_behavior': 'pause_behavior_example',
        'status': openapi_server.CallRecordingEnumStatus()
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Recordings/{sid_jso}'.format(account_sid='account_sid_example', call_sid='call_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_conference_recording(client):
    """Test case for update_conference_recording

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'pause_behavior': 'pause_behavior_example',
        'status': openapi_server.ConferenceRecordingEnumStatus()
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings/{sid_jso}'.format(account_sid='account_sid_example', conference_sid='conference_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

