# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_call_response import BulkCallResponse
from openapi_server.models.call_response import CallResponse
from openapi_server.models.cancel_scheduled_hangup_response import CancelScheduledHangupResponse
from openapi_server.models.cancel_scheduled_play_response import CancelScheduledPlayResponse
from openapi_server.models.group_call_response import GroupCallResponse
from openapi_server.models.hangup_all_calls_response import HangupAllCallsResponse
from openapi_server.models.hangup_call_response import HangupCallResponse
from openapi_server.models.play_response import PlayResponse
from openapi_server.models.play_stop_response import PlayStopResponse
from openapi_server.models.record_start_response import RecordStartResponse
from openapi_server.models.record_stop_response import RecordStopResponse
from openapi_server.models.schedule_hangup_response import ScheduleHangupResponse
from openapi_server.models.schedule_play_response import SchedulePlayResponse
from openapi_server.models.send_digits_response import SendDigitsResponse
from openapi_server.models.sound_touch_response import SoundTouchResponse
from openapi_server.models.sound_touch_stop_response import SoundTouchStopResponse
from openapi_server.models.transfer_call_response import TransferCallResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_bulk_call_post(client):
    """Test case for v01_bulk_call_post

    /v0.1/BulkCall/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'answer_url': 'answer_url_example',
        'caller_name': 'caller_name_example',
        'confirm_key': 'confirm_key_example',
        'confirm_sound': 'confirm_sound_example',
        'core_uuid': 'core_uuid_example',
        'delimiter': 'delimiter_example',
        'extra_dial_string': 'extra_dial_string_example',
        '_from': '_from_example',
        'gateway_codecs': 'gateway_codecs_example',
        'gateway_retries': 'gateway_retries_example',
        'gateway_timeouts': 'gateway_timeouts_example',
        'gateways': 'gateways_example',
        'hangup_on_ring': 56,
        'hangup_url': 'hangup_url_example',
        'reject_causes': 'NO_ANSWER,ORIGINATOR_CANCEL,ALLOTTED_TIMEOUT,NO_USER_RESPONSE,CALL_REJECTED',
        'ring_url': 'ring_url_example',
        'send_digits': 'send_digits_example',
        'send_on_preanswer': True,
        'time_limit': 56,
        'to': 'to_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/BulkCall/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_call_post(client):
    """Test case for v01_call_post

    /v0.1/Call/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'answer_url': 'answer_url_example',
        'async_amd': False,
        'async_amd_status_callback': 'async_amd_status_callback_example',
        'async_amd_status_callback_method': POST,
        'caller_name': 'caller_name_example',
        'core_uuid': 'core_uuid_example',
        'extra_dial_string': 'extra_dial_string_example',
        '_from': '_from_example',
        'gateway_codecs': 'gateway_codecs_example',
        'gateway_retries': 'gateway_retries_example',
        'gateway_timeouts': 'gateway_timeouts_example',
        'gateways': 'gateways_example',
        'hangup_on_ring': 56,
        'hangup_url': 'hangup_url_example',
        'machine_detection': 'machine_detection_example',
        'machine_detection_silence_timeout': 5000,
        'machine_detection_speech_end_threshold': 1200,
        'machine_detection_speech_threshold': 2400,
        'machine_detection_timeout': 30,
        'ring_url': 'ring_url_example',
        'send_digits': 'send_digits_example',
        'send_on_preanswer': True,
        'time_limit': 56,
        'to': 'to_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/Call/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_cancel_scheduled_hangup_post(client):
    """Test case for v01_cancel_scheduled_hangup_post

    /v0.1/CancelScheduledHangup/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'sched_hangup_id': 'sched_hangup_id_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/CancelScheduledHangup/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_cancel_scheduled_play_post(client):
    """Test case for v01_cancel_scheduled_play_post

    /v0.1/CancelScheduledPlay/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'sched_play_id': 'sched_play_id_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/CancelScheduledPlay/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_group_call_post(client):
    """Test case for v01_group_call_post

    /v0.1/GroupCall/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'answer_url': 'answer_url_example',
        'caller_name': 'caller_name_example',
        'confirm_key': 'confirm_key_example',
        'confirm_sound': 'confirm_sound_example',
        'core_uuid': 'core_uuid_example',
        'delimiter': 'delimiter_example',
        'extra_dial_string': 'extra_dial_string_example',
        '_from': '_from_example',
        'gateway_codecs': 'gateway_codecs_example',
        'gateway_retries': 'gateway_retries_example',
        'gateway_timeouts': 'gateway_timeouts_example',
        'gateways': 'gateways_example',
        'hangup_on_ring': 56,
        'hangup_url': 'hangup_url_example',
        'reject_causes': 'NO_ANSWER,ORIGINATOR_CANCEL,ALLOTTED_TIMEOUT,NO_USER_RESPONSE,CALL_REJECTED',
        'ring_url': 'ring_url_example',
        'send_digits': 'send_digits_example',
        'send_on_preanswer': True,
        'time_limit': 56,
        'to': 'to_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/GroupCall/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v01_hangup_all_calls_post(client):
    """Test case for v01_hangup_all_calls_post

    /v0.1/HangupAllCalls/
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/HangupAllCalls/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_hangup_call_post(client):
    """Test case for v01_hangup_call_post

    /v0.1/HangupCall/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid': 'call_uuid_example',
        'request_uuid': 'request_uuid_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/HangupCall/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_play_post(client):
    """Test case for v01_play_post

    /v0.1/Play/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid': 'call_uuid_example',
        'legs': aleg,
        'length': 3600,
        'loop': False,
        'mix': True,
        'sounds': 'sounds_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/Play/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_play_stop_post(client):
    """Test case for v01_play_stop_post

    /v0.1/PlayStop/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid': 'call_uuid_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/PlayStop/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_record_start_post(client):
    """Test case for v01_record_start_post

    /v0.1/RecordStart/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid': 'call_uuid_example',
        'file_format': mp3,
        'file_name': '',
        'file_path': '',
        'time_limit': 60
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/RecordStart/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_record_stop_post(client):
    """Test case for v01_record_stop_post

    /v0.1/RecordStop/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid': 'call_uuid_example',
        'record_file': 'record_file_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/RecordStop/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_schedule_hangup_post(client):
    """Test case for v01_schedule_hangup_post

    /v0.1/ScheduleHangup/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid': 'call_uuid_example',
        'time': 56
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/ScheduleHangup/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_schedule_play_post(client):
    """Test case for v01_schedule_play_post

    /v0.1/SchedulePlay/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid': 'call_uuid_example',
        'legs': aleg,
        'length': 3600,
        'loop': False,
        'mix': True,
        'sounds': 'sounds_example',
        'time': 56
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/SchedulePlay/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_send_digits_post(client):
    """Test case for v01_send_digits_post

    /v0.1/SendDigits/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid': 'call_uuid_example',
        'digits': 'digits_example',
        'leg': aleg
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/SendDigits/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_sound_touch_post(client):
    """Test case for v01_sound_touch_post

    /v0.1/SoundTouch/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'audio_direction': out,
        'call_uuid': 'call_uuid_example',
        'pitch': 1,
        'pitch_octaves': 3.4,
        'pitch_semi_tones': 3.4,
        'rate': 1,
        'tempo': 1
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/SoundTouch/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_sound_touch_stop_post(client):
    """Test case for v01_sound_touch_stop_post

    /v0.1/SoundTouchStop/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid': 'call_uuid_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/SoundTouchStop/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v01_transfer_call_post(client):
    """Test case for v01_transfer_call_post

    /v0.1/TransferCall/
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'call_uuid': 'call_uuid_example',
        'url': 'url_example'
        }
    response = await client.request(
        method='POST',
        path='/rtckit/media/master/eqivo/readme-splash.png/v0.1/TransferCall/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

