# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_v2010_account_call import ApiV2010AccountCall
from openapi_server.models.call_enum_status import CallEnumStatus
from openapi_server.models.call_enum_update_status import CallEnumUpdateStatus
from openapi_server.models.list_call_response import ListCallResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_call(client):
    """Test case for create_call

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'application_sid': 'application_sid_example',
        'async_amd': 'async_amd_example',
        'async_amd_status_callback': 'async_amd_status_callback_example',
        'async_amd_status_callback_method': 'async_amd_status_callback_method_example',
        'byoc': 'byoc_example',
        'call_reason': 'call_reason_example',
        'call_token': 'call_token_example',
        'caller_id': 'caller_id_example',
        'fallback_method': 'fallback_method_example',
        'fallback_url': 'fallback_url_example',
        '_from': '_from_example',
        'machine_detection': 'machine_detection_example',
        'machine_detection_silence_timeout': 56,
        'machine_detection_speech_end_threshold': 56,
        'machine_detection_speech_threshold': 56,
        'machine_detection_timeout': 56,
        'method': 'method_example',
        'record': True,
        'recording_channels': 'recording_channels_example',
        'recording_status_callback': 'recording_status_callback_example',
        'recording_status_callback_event': ['recording_status_callback_event_example'],
        'recording_status_callback_method': 'recording_status_callback_method_example',
        'recording_track': 'recording_track_example',
        'send_digits': 'send_digits_example',
        'sip_auth_password': 'sip_auth_password_example',
        'sip_auth_username': 'sip_auth_username_example',
        'status_callback': 'status_callback_example',
        'status_callback_event': ['status_callback_event_example'],
        'status_callback_method': 'status_callback_method_example',
        'time_limit': 56,
        'timeout': 56,
        'to': 'to_example',
        'trim': 'trim_example',
        'twiml': 'twiml_example',
        'url': 'url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Calls.json'.format(account_sid='account_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_call(client):
    """Test case for delete_call

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_call(client):
    """Test case for fetch_call

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_call(client):
    """Test case for list_call

    
    """
    params = [('To', 'to_example'),
                    ('From', '_from_example'),
                    ('ParentCallSid', 'parent_call_sid_example'),
                    ('Status', openapi_server.CallEnumStatus()),
                    ('StartTime', '2013-10-20T19:20:30+01:00'),
                    ('StartTime&lt;', '2013-10-20T19:20:30+01:00'),
                    ('StartTime&gt;', '2013-10-20T19:20:30+01:00'),
                    ('EndTime', '2013-10-20T19:20:30+01:00'),
                    ('EndTime&lt;', '2013-10-20T19:20:30+01:00'),
                    ('EndTime&gt;', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/2010-04-01/Accounts/{account_sid}/Calls.json'.format(account_sid='account_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_call(client):
    """Test case for update_call

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'fallback_method': 'fallback_method_example',
        'fallback_url': 'fallback_url_example',
        'method': 'method_example',
        'status': openapi_server.CallEnumUpdateStatus(),
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example',
        'time_limit': 56,
        'twiml': 'twiml_example',
        'url': 'url_example'
        }
    response = await client.request(
        method='POST',
        path='/2010-04-01/Accounts/{account_sid}/Calls/{sid_jso}'.format(account_sid='account_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

