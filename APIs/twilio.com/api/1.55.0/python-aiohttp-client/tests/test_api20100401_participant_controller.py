# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_conference_participant import ApiV2010AccountConferenceParticipant
from openapi_server.models.list_participant_response import ListParticipantResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_participant(client):
    """Test case for create_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'amd_status_callback': 'amd_status_callback_example',
        'amd_status_callback_method': 'amd_status_callback_method_example',
        'beep': 'beep_example',
        'byoc': 'byoc_example',
        'call_reason': 'call_reason_example',
        'call_sid_to_coach': 'call_sid_to_coach_example',
        'call_token': 'call_token_example',
        'caller_id': 'caller_id_example',
        'coaching': True,
        'conference_record': 'conference_record_example',
        'conference_recording_status_callback': 'conference_recording_status_callback_example',
        'conference_recording_status_callback_event': ['conference_recording_status_callback_event_example'],
        'conference_recording_status_callback_method': 'conference_recording_status_callback_method_example',
        'conference_status_callback': 'conference_status_callback_example',
        'conference_status_callback_event': ['conference_status_callback_event_example'],
        'conference_status_callback_method': 'conference_status_callback_method_example',
        'conference_trim': 'conference_trim_example',
        'early_media': True,
        'end_conference_on_exit': True,
        '_from': '_from_example',
        'jitter_buffer_size': 'jitter_buffer_size_example',
        'label': 'label_example',
        'machine_detection': 'machine_detection_example',
        'machine_detection_silence_timeout': 56,
        'machine_detection_speech_end_threshold': 56,
        'machine_detection_speech_threshold': 56,
        'machine_detection_timeout': 56,
        'max_participants': 56,
        'muted': True,
        'record': True,
        'recording_channels': 'recording_channels_example',
        'recording_status_callback': 'recording_status_callback_example',
        'recording_status_callback_event': ['recording_status_callback_event_example'],
        'recording_status_callback_method': 'recording_status_callback_method_example',
        'recording_track': 'recording_track_example',
        'region': 'region_example',
        'sip_auth_password': 'sip_auth_password_example',
        'sip_auth_username': 'sip_auth_username_example',
        'start_conference_on_enter': True,
        'status_callback': 'status_callback_example',
        'status_callback_event': ['status_callback_event_example'],
        'status_callback_method': 'status_callback_method_example',
        'time_limit': 56,
        'timeout': 56,
        'to': 'to_example',
        'trim': 'trim_example',
        'wait_method': 'wait_method_example',
        'wait_url': 'wait_url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants.json'.format(account_sid='account_sid_example', conference_sid='conference_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_participant(client):
    """Test case for delete_participant

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_jso}'.format(account_sid='account_sid_example', conference_sid='conference_sid_example', call_sid='call_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_participant(client):
    """Test case for fetch_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_jso}'.format(account_sid='account_sid_example', conference_sid='conference_sid_example', call_sid='call_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_participant(client):
    """Test case for list_participant

    
    """
    params = [('Muted', True),
                    ('Hold', True),
                    ('Coaching', True),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants.json'.format(account_sid='account_sid_example', conference_sid='conference_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_participant(client):
    """Test case for update_participant

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'announce_method': 'announce_method_example',
        'announce_url': 'announce_url_example',
        'beep_on_exit': True,
        'call_sid_to_coach': 'call_sid_to_coach_example',
        'coaching': True,
        'end_conference_on_exit': True,
        'hold': True,
        'hold_method': 'hold_method_example',
        'hold_url': 'hold_url_example',
        'muted': True,
        'wait_method': 'wait_method_example',
        'wait_url': 'wait_url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Conferences/{conference_sid}/Participants/{call_sid_jso}'.format(account_sid='account_sid_example', conference_sid='conference_sid_example', call_sid='call_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

